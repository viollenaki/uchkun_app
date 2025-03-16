from django.urls import path
from . import views

urlpatterns = [
    path('add_university/', views.UniversityCreateView.as_view(), name='add_university'),
    path('add_professor/', views.ProfessorCreateView.as_view(), name='add_professor'),
    path('add_student/', views.StudentCreateView.as_view(), name='add_student'),
    path('add_subject/', views.SubjectCreateView.as_view(), name='add_subject'),
]