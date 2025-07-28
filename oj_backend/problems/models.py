from django.db import models
from django.contrib.auth.models import User

# Create your models here.

DIFFICULTY_CHOICES = [
    ("Easy", "Easy"),
    ("Medium", "Medium"),
    ("Hard", "Hard"),
]

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Problem(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField()
    difficulty = models.CharField(
        max_length=10,
        blank=True,
        choices=DIFFICULTY_CHOICES,
    )
    tags = models.ManyToManyField(Tag, related_name='problems')
    constraints = models.TextField(blank=True)
    def __str__(self):
        return f"{self.id}"
    
class Submission(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    language = models.CharField(max_length=100)
    code = models.TextField()
    verdict = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

class RunCode(models.Model):
    language = models.CharField(max_length=100)
    code = models.TextField()
    input_data = models.TextField(null=True, blank=True)
    output_data = models.TextField(null=True, blank=True)


class TestCases(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    input_data = models.TextField(null=True, blank=True)
    output_data = models.TextField(null=True, blank=True)

class Example(models.Model):
    problem = models.ForeignKey(Problem, related_name='examples', on_delete=models.CASCADE)
    input = models.TextField()
    output = models.TextField()
    explanation = models.TextField(blank=True)

    def __str__(self):
        return f"Example for {self.problem.title}"