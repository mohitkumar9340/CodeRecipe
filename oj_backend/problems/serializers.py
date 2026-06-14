from rest_framework import serializers
from .models import Problem, TestCases, Submission, RunCode, Tag, Example


class ProblemSerializer(serializers.ModelSerializer):
    tag_names = serializers.SerializerMethodField()

    class Meta:
        model = Problem
        fields = ['id', 'title', 'description', 'input_format', 'output_format',
                  'difficulty', 'tag_names', 'constraints', 'time_limit', 'memory_limit']

    def get_tag_names(self, obj):
        return [tag.name for tag in obj.tags.all()]


class ProblemListSerializer(serializers.ModelSerializer):
    tag_names = serializers.SerializerMethodField()
    user_status = serializers.SerializerMethodField()

    class Meta:
        model = Problem
        fields = ['id', 'title', 'difficulty', 'tag_names', 'user_status']

    def get_tag_names(self, obj):
        return [tag.name for tag in obj.tags.all()]

    def get_user_status(self, obj):
        request = self.context.get('request')
        if not request or not request.user.is_authenticated:
            return 'Unsolved'
        submissions = Submission.objects.filter(problem=obj, user=request.user)
        if not submissions.exists():
            return 'Unsolved'
        if submissions.filter(verdict='All testcases passed').exists():
            return 'Solved'
        return 'Attempted'


class AddProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = "__all__"


class AddTestCaseSeriallzer(serializers.ModelSerializer):
    class Meta:
        model = TestCases
        fields = "__all__"


class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = "__all__"
        read_only_fields = ['verdict', 'user', 'timestamp', 'execution_time', 'memory_used']


class RunCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RunCode
        fields = ['code', 'language', 'input_data']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class ExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Example
        fields = "__all__"
