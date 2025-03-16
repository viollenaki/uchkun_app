from django.urls import path
from . import views

urlpatterns = [

    path('choose_subjects/', views.ChooseSubjectsView.as_view(), name='add_subject')

]