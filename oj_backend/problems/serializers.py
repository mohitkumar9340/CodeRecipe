from rest_framework import serializers
from .models import Problem, TestCases, Submission, RunCode, Tag, Example


class ProblemSerializer(serializers.ModelSerializer):
    tag_names = serializers.SerializerMethodField()  # Custom field to get tag names

    class Meta:
        model = Problem
        fields = ['id', 'title', 'description', 'difficulty', 'tag_names', 'constraints']  # Exclude 'tags'

    def get_tag_names(self, obj):
        # Explicitly return tag names
        return [tag.name for tag in obj.tags.all()]

class AddProblemSerializer(serializers.ModelSerializer):
    # title = serializers.CharField(required=True)
    # description = serializers.CharField(required=True)
    # difficulty = serializers.CharField()
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

class RunCodeSerializer(serializers.ModelSerializer):
    # code = serializers.CharField()
    # language = serializers.CharField()
    # input_data = serializers.CharField()
    class Meta:
        model = RunCode
        fields = ['code', 'language', 'input_data']
        # extra_kwargs = {
        #     'input_data': {'required': False, 'allow_blank': True}
        # }

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"

class ExampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Example
        fields = "__all__" 