from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Problem, TestCases, Submission, Tag, Example
from .serializers import ProblemSerializer, AddProblemSerializer, AddTestCaseSeriallzer, SubmissionSerializer, RunCodeSerializer, TagSerializer, ExampleSerializer
from rest_framework.response import Response
from .judge.compiler import Compiler
from .judge.judge import Judge
from rest_framework.permissions import AllowAny
from datetime import datetime
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
compiler = Compiler()
judge = Judge()
# Create your views here.

class AddProblemAPIView(APIView):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer

    # authentication_classes = [JWTAuthentication]  # Use JWT authentication
    # permission_classes = [IsAuthenticated]  # Require authentication to access the API

    def post(self, request):
        serializer = AddProblemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            title = serializer.data["title"]
            description = serializer.data["description"]
            difficulty = serializer.data["difficulty"]
            problem = Problem.objects.create(title=title, description=description, difficulty=difficulty)
            problem.save()
            print("saved")
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    def get(self, request):
        problems = Problem.objects.filter()
        serializer = ProblemSerializer(problems, many=True)
        return Response(serializer.data, status=201)

class ProblemListAPIView(APIView):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer

    # authentication_classes = [JWTAuthentication]  # Use JWT authentication
    permission_classes = [AllowAny]  # Require authentication to access the API

    def get(self, request):
        problems = Problem.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(problems, 4)
        try:
            paginated_problems = paginator.page(page)  # Get the specific page
        except PageNotAnInteger:
            paginated_problems = paginator.page(1)  # Default to page 1 if page is not an integer
        except EmptyPage:
            paginated_problems = paginator.page(paginator.num_pages)
        serializer = ProblemSerializer(paginated_problems, many=True)
        return Response({
            'problems': serializer.data,  # Paginated problem data
            'total_pages': paginator.num_pages,  # Total number of pages
            'current_page': paginated_problems.number,  # Current page number
            'total_problems': paginator.count
        }, status=200)
        # return Response(serializer.data, status = 201)
    

    
class ProblemDetailAPIView(APIView):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer
    # lookup_field = "code"
    permission_classes = [AllowAny]  # Require authentication to access the API

    def get(self, request, *args, **kwargs):
        # breakpoint()
        problem_id = self.kwargs['id']
        problem = Problem.objects.get(id=problem_id)
        serializer = ProblemSerializer(problem)
        print(serializer)
        print(serializer.data)
        examples = Example.objects.filter(problem=problem)
        examples_serializer = ExampleSerializer(examples, many=True)
        response_data = serializer.data
        response_data['examples'] = examples_serializer.data
        return Response(response_data, status=201)
    # authentication_classes = [JWTAuthentication]  # Use JWT authentication
    # permission_classes = [IsAuthenticated]

class AddTestCaseAPIView(APIView):
    # authentication_classes = [JWTAuthentication]  # Use JWT authentication
    # permission_classes = [IsAuthenticated]
    serializer_class = AddTestCaseSeriallzer
    permission_classes = [AllowAny]  # Require authentication to access the API

    def post(self, request):
        serializer = AddTestCaseSeriallzer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # problemid = serializer.data["problem"]
            # input_data = serializer.data["input_data"]
            # output_data = serializer.data["output_data"]
            # problem = Problem.objects.get(id=problemid)
            # testcase = TestCases.objects.create(problem=problem, input_data=input_data, output_data=output_data)
            # testcase.save()
            # print("saved")
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)



class SubmitCodeAPIView(APIView):
    # authentication_classes = [JWTAuthentication]  # Use JWT authentication
    # permission_classes = [IsAuthenticated]
    serializer_class = SubmissionSerializer
    permission_classes = [AllowAny]  # Require authentication to access the API
    def post(self, request):
        print(request)
        print(request.data)
        serializer = SubmissionSerializer(data=request.data)
        # breakpoint()
        print("serializer: ", serializer)
        if serializer.is_valid():
            print("serializer is valid")
            # serializer.save()

            language = serializer.data["language"]
            code = serializer.data["code"]
            problem_id = serializer.data["problem"]
            verdict = judge.run_testcases(problem_id=problem_id, language=language, code=code)
            user = request.user
            time = datetime.now()
            problem = Problem.objects.get(id=problem_id)
            submission = Submission.objects.create(problem=problem, language=language, code=code, verdict=verdict, user=user, timestamp=time)
            submission.save()
            return Response(verdict, status=201)
        print(request.data)
        return Response(serializer.errors, status=400)
    
class RunCodeAPIView(APIView):
    # authentication_classes = [JWTAuthentication]  # Use JWT authentication
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    serializer_class = RunCodeSerializer
    def post(self, request):
        # code = request.data["code"]
        # language = request.data["language"]
        # input_data = request.data.get("input_data", "")
        serializer = RunCodeSerializer(data=request.data)
        if serializer.is_valid():
            # serializer.save()
            language = serializer.data["language"]
            code = serializer.data["code"]
            input_data = serializer.data.get("input_data", "")
            print(language, code, input_data)
            res = compiler.run_code(language=language, code=code, input_data=input_data)
            return Response(res, status=201)
        return Response(serializer.errors, status=400)
    
class AddTagAPIView(APIView):
    # authentication_classes = [JWTAuthentication]  # Use JWT authentication
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    serializer_class = TagSerializer
    def post(self, request):
        serializer = TagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class TagListAPIView(APIView):
    # authentication_classes = [JWTAuthentication]  # Use JWT authentication
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    serializer_class = TagSerializer
    def get(self, request):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data, status=201)
    
class SubmissionListAPIView(APIView):
    # authentication_classes = [JWTAuthentication]  # Use JWT authentication
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    serializer_class = SubmissionSerializer
    def get(self, request):
        problem_id = self.kwargs['id']
        problem = Problem.objects.get(id=problem_id)
        submissions = Submission.objects.filter(problem=problem)
        serializer = SubmissionSerializer(submissions, many=True)
        return Response(serializer.data, status=201)
    
class UserSubmissionListAPIView(APIView):
    # authentication_classes = [JWTAuthentication]  # Use JWT authentication
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    serializer_class = SubmissionSerializer
    def get(self, request):
        user = request.user
        problem_id = self.kwargs['id']
        problem = Problem.objects.get(id=problem_id)
        submissions = Submission.objects.filter(user=user, problem=problem)
        serializer = SubmissionSerializer(submissions, many=True)
        return Response(serializer.data, status=201)