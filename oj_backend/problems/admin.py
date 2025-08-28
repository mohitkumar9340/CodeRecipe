from django.contrib import admin
from .models import Problem, Submission, TestCases, Tag, Example

# Register your models here.
admin.site.register(Problem)
admin.site.register(Submission)
admin.site.register(TestCases)
admin.site.register(Tag)
admin.site.register(Example)