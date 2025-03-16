from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.contrib.auth.hashers import check_password, make_password

from admin_url.models import *


# Create your views here.

class ChooseSubjectsView(APIView):

    
    def post(self, request):
        data = request.data
        stud_id = data['stud_id']
        subjects = data['subjects'].split(',')

        if not Student.objects.filter(stud_id=stud_id).exists():
            return Response({'message': 'Student does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        
        student = Student.objects.get(stud_id=stud_id)
        for subject in subjects:
            if not Subject.objects.filter(name=subject).exists():
                return Response({'message': 'Subject does not exist'}, status=status.HTTP_400_BAD_REQUEST)
            
        sub_set = set()

        for i in Registration.objects.filter(student=student):
            sub_set.add(i.subject.name)

        for subject in subjects:
            if subject in sub_set:
                return Response({'message': 'Subject already registered'}, status=status.HTTP_400_BAD_REQUEST)

        for subject in subjects:
            subject_obj = Subject.objects.get(name=subject)
            Registration.objects.create(student=student, subject=subject_obj)




        return Response({'message': 'Subjects added successfully'}, status=status.HTTP_201_CREATED)