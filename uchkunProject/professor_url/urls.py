from django.urls import path
from . import views

urlpatterns = [

    path('add_grade/', views.AddGradeView.as_view(), name='add_grade'),

]