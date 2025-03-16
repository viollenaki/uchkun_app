from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from admin_url.models import * 

# Create your views here.


class AddGradeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        stud_id = data['stud_id']
        subject = data['subject']
        grade = data['grade']

        if not Student.objects.filter(stud_id=stud_id).exists():
            return Response({'message': 'Student does not exist'}, status=status.HTTP_400_BAD_REQUEST)

        if not Subject.objects.filter(name=subject).exists():
            return Response({'message': 'Subject does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        
        student = Student.objects.get(stud_id=stud_id)
        subject_obj = Subject.objects.get(name=subject)
        grade_obj = Grades.objects.create(student=student, subject=subject_obj, grade=grade)
        return Response({'message': 'Grade added successfully'}, status=status.HTTP_201_CREATED)

        