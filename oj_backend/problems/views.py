from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Problem, TestCases, Submission, Tag, Example
from .serializers import (
    ProblemSerializer, ProblemListSerializer, AddProblemSerializer,
    AddTestCaseSerializer, SubmissionSerializer, RunCodeSerializer,
    TagSerializer, ExampleSerializer, SubmitCodeSerializer
)
from rest_framework.response import Response
from .judge.compiler import Compiler
from .judge.judge import Judge
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Exists, OuterRef

compiler = Compiler()
judge = Judge()


class AddProblemAPIView(APIView):
    def post(self, request):
        serializer = AddProblemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Problem created successfully", **serializer.data}, status=201)
        errors = serializer.errors
        first = next(iter(errors.values()))
        msg = first[0] if isinstance(first, list) else first
        return Response({"message": msg, "errors": errors}, status=400)


class ProblemListAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        problems = Problem.objects.all().prefetch_related('tags')

        difficulty = request.GET.get('difficulty')
        if difficulty:
            problems = problems.filter(difficulty=difficulty)

        search = request.GET.get('search')
        if search:
            problems = problems.filter(title__icontains=search)

        tags = request.GET.get('tags')
        if tags:
            tag_list = [t.strip() for t in tags.split(',') if t.strip()]
            for tag_name in tag_list:
                problems = problems.filter(tags__name=tag_name)

        if request.user.is_authenticated:
            problems = problems.annotate(
                has_submission=Exists(
                    Submission.objects.filter(
                        problem=OuterRef('pk'), user=request.user
                    )
                ),
                has_accepted=Exists(
                    Submission.objects.filter(
                        problem=OuterRef('pk'), user=request.user,
                        verdict='All testcases passed'
                    )
                ),
            )

            status = request.GET.get('status')
            if status == 'solved':
                problems = problems.filter(has_accepted=True)
            elif status == 'attempted':
                problems = problems.filter(has_submission=True, has_accepted=False)
            elif status == 'unsolved':
                problems = problems.filter(has_submission=False)

        try:
            page = int(request.GET.get('page', 1))
        except (ValueError, TypeError):
            page = 1
        paginator = Paginator(problems, 20)
        try:
            paginated_problems = paginator.page(page)
        except PageNotAnInteger:
            paginated_problems = paginator.page(1)
        except EmptyPage:
            paginated_problems = paginator.page(paginator.num_pages)

        serializer = ProblemListSerializer(
            paginated_problems, many=True, context={'request': request}
        )
        return Response({
            'problems': serializer.data,
            'total_pages': paginator.num_pages,
            'current_page': paginated_problems.number,
            'total_problems': paginator.count
        }, status=200)


class ProblemDetailAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        problem_id = self.kwargs['id']
        try:
            problem = Problem.objects.get(id=problem_id)
        except Problem.DoesNotExist:
            return Response({"message": "Problem not found"}, status=404)

        serializer = ProblemSerializer(problem)
        examples = Example.objects.filter(problem=problem)
        examples_serializer = ExampleSerializer(examples, many=True)
        response_data = serializer.data
        response_data['examples'] = examples_serializer.data

        if request.user.is_authenticated:
            submissions = Submission.objects.filter(problem=problem, user=request.user)
            if not submissions.exists():
                response_data['user_status'] = 'Unsolved'
            elif submissions.filter(verdict='All testcases passed').exists():
                response_data['user_status'] = 'Solved'
            else:
                response_data['user_status'] = 'Attempted'
        else:
            response_data['user_status'] = 'Unsolved'

        return Response(response_data, status=200)


class AddTestCaseAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = AddTestCaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Test case added successfully", **serializer.data}, status=201)
        errors = serializer.errors
        first = next(iter(errors.values()))
        msg = first[0] if isinstance(first, list) else first
        return Response({"message": msg, "errors": errors}, status=400)


class SubmitCodeAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = SubmitCodeSerializer(data=request.data)
        if not serializer.is_valid():
            errors = serializer.errors
            first = next(iter(errors.values()))
            msg = first[0] if isinstance(first, list) else first
            return Response({"message": msg, "errors": errors}, status=400)

        language = serializer.validated_data["language"]
        code = serializer.validated_data["code"]
        problem_id = serializer.validated_data["problem"]

        try:
            problem = Problem.objects.get(id=problem_id)
        except Problem.DoesNotExist:
            return Response({"message": "Problem not found"}, status=404)

        judge_result = judge.run_testcases(
            problem_id=problem_id, language=language, code=code
        )
        verdict_str = judge_result['verdict']

        submission_data = {
            'problem': problem,
            'language': language,
            'code': code,
            'verdict': verdict_str,
            'timestamp': timezone.now(),
            'execution_time': judge_result.get('execution_time', 0),
            'memory_used': judge_result.get('memory_used', 0),
        }
        if request.user.is_authenticated:
            submission_data['user'] = request.user

        submission = Submission.objects.create(**submission_data)

        response_data = {
            'message': 'Solution submitted successfully',
            'id': submission.id,
            'verdict': verdict_str,
            'results': judge_result['results'],
            'execution_time': judge_result.get('execution_time', 0),
            'memory_used': judge_result.get('memory_used', 0),
        }
        return Response(response_data, status=200)


class RunCodeAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RunCodeSerializer(data=request.data)
        if serializer.is_valid():
            language = serializer.validated_data["language"]
            code = serializer.validated_data["code"]
            input_data = serializer.validated_data.get("input_data", "")
            res = compiler.run_code(language=language, code=code, input_data=input_data)
            return Response({"message": "Code executed successfully", **res}, status=200)
        errors = serializer.errors
        first = next(iter(errors.values()))
        msg = first[0] if isinstance(first, list) else first
        return Response({"message": msg, "errors": errors}, status=400)


class AddTagAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Tag added successfully", **serializer.data}, status=201)
        errors = serializer.errors
        first = next(iter(errors.values()))
        msg = first[0] if isinstance(first, list) else first
        return Response({"message": msg, "errors": errors}, status=400)


class TagListAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data, status=200)


class SubmissionListAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        problem_id = request.GET.get('id')
        if not problem_id:
            return Response({"message": "Missing problem id"}, status=400)

        try:
            problem = Problem.objects.get(id=problem_id)
        except Problem.DoesNotExist:
            return Response({"message": "Problem not found"}, status=404)

        if not request.user.is_authenticated:
            return Response({"message": "Authentication required"}, status=401)

        submissions = Submission.objects.filter(
            user=request.user, problem=problem
        ).order_by('-timestamp')

        serializer = SubmissionSerializer(submissions, many=True)
        return Response(serializer.data, status=200)
