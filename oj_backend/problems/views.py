from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Problem, TestCases, Submission, Tag, Example
from .serializers import (
    ProblemSerializer, ProblemListSerializer, AddProblemSerializer,
    AddTestCaseSeriallzer, SubmissionSerializer, RunCodeSerializer,
    TagSerializer, ExampleSerializer
)
from rest_framework.response import Response
from .judge.compiler import Compiler
from .judge.judge import Judge
from datetime import datetime
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

compiler = Compiler()
judge = Judge()


class AddProblemAPIView(APIView):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer

    def post(self, request):
        serializer = AddProblemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def get(self, request):
        problems = Problem.objects.filter()
        serializer = ProblemSerializer(problems, many=True)
        return Response(serializer.data, status=200)


class ProblemListAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        problems = Problem.objects.all().prefetch_related('tags')
        page = request.GET.get('page', 1)
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
        problem = Problem.objects.get(id=problem_id)
        serializer = ProblemSerializer(problem)
        examples = Example.objects.filter(problem=problem)
        examples_serializer = ExampleSerializer(examples, many=True)
        response_data = serializer.data
        response_data['examples'] = examples_serializer.data

        # Add user status
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
    serializer_class = AddTestCaseSeriallzer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = AddTestCaseSeriallzer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class SubmitCodeAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        language = request.data.get("language")
        code = request.data.get("code")
        problem_id = request.data.get("problem")

        if not all([language, code, problem_id]):
            return Response({"error": "Missing required fields"}, status=400)

        judge_result = judge.run_testcases(
            problem_id=problem_id, language=language, code=code
        )
        verdict_str = judge_result['verdict']
        time_now = datetime.now()
        problem = Problem.objects.get(id=problem_id)

        submission_data = {
            'problem': problem,
            'language': language,
            'code': code,
            'verdict': verdict_str,
            'timestamp': time_now,
            'execution_time': judge_result.get('execution_time', 0),
            'memory_used': judge_result.get('memory_used', 0),
        }
        if request.user.is_authenticated:
            submission_data['user'] = request.user

        submission = Submission.objects.create(**submission_data)

        response_data = {
            'id': submission.id,
            'verdict': verdict_str,
            'results': judge_result['results'],
            'execution_time': judge_result.get('execution_time', 0),
            'memory_used': judge_result.get('memory_used', 0),
        }
        return Response(response_data, status=201)


class RunCodeAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RunCodeSerializer(data=request.data)
        if serializer.is_valid():
            language = serializer.data["language"]
            code = serializer.data["code"]
            input_data = serializer.data.get("input_data", "")
            res = compiler.run_code(language=language, code=code, input_data=input_data)
            return Response(res, status=200)
        return Response(serializer.errors, status=400)


class AddTagAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


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
        problem = Problem.objects.get(id=problem_id)

        if request.user.is_authenticated:
            submissions = Submission.objects.filter(
                user=request.user, problem=problem
            ).order_by('-timestamp')
        else:
            submissions = Submission.objects.filter(
                problem=problem
            ).order_by('-timestamp')

        serializer = SubmissionSerializer(submissions, many=True)
        return Response(serializer.data, status=200)
