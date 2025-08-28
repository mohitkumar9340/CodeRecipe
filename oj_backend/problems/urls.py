from django.urls import path
from . import views


urlpatterns = [
    path('problems/', views.ProblemListAPIView.as_view(), name='problems'),
    path('add-problem/', views.AddProblemAPIView.as_view(), name='add-problem'),
    path('add-test-case/', views.AddTestCaseAPIView.as_view(), name='add-test-case'),
    path('submit/', views.SubmitCodeAPIView.as_view(), name='submit'),
    path('run/', views.RunCodeAPIView.as_view(), name='run'),
    path('problems/<str:id>/', views.ProblemDetailAPIView.as_view(), name='problem-detail'),
    path('add-tag/', views.AddTagAPIView.as_view(), name='add-tag'),
    path('tags/', views.TagListAPIView.as_view(), name='tags'),
    path('submissionsAll/', views.SubmissionListAPIView.as_view(), name='submissions'),
    path('submissionsUser/', views.UserSubmissionListAPIView.as_view(), name='user-submissions'),
]
