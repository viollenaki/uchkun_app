from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.contrib.auth.hashers import check_password, make_password
from rest_framework.permissions import IsAuthenticated


from .models import *


# Create your views here.
class UniversityCreateView(APIView):
    permission_classes = [IsAuthenticated] 


    def post(self, request):
        data = request.data
        if University.objects.filter(name=data['name']).exists():
            return Response({'message': 'University already exists'}, status=status.HTTP_400_BAD_REQUEST)
        university = University.objects.create(name=data['name'])
        return Response({'message': 'University created successfully'}, status=status.HTTP_201_CREATED)
    

class ProfessorCreateView(APIView):
    parser_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data
        if Professor.objects.filter(name=data['name']).exists():
            return Response({'message': 'Professor already exists'}, status=status.HTTP_400_BAD_REQUEST)
        name = data['name']
        univ = data['university']
        univ_obj = University.objects.get(name=univ)
        professor = Professor.objects.create(name=name, university=univ_obj)
        return Response({'message': 'Professor created successfully'}, status=status.HTTP_201_CREATED)
    
class StudentCreateView(APIView):
    parser_classes = [IsAuthenticated]


    def post(self, request):
        data = request.data
        stud_id = data['stud_id']
        name = data['name']
        univ = data['university']
        if Student.objects.filter(stud_id=stud_id).exists():
            return Response({'message': 'Student already exists'}, status=status.HTTP_400_BAD_REQUEST)
        
        if not University.objects.filter(name=univ).exists():
            return Response({'message': 'University does not exist'}, status=status.HTTP_400_BAD_REQUEST)

        univ_obj = University.objects.get(name=univ)
        student = Student.objects.create(stud_id=stud_id, name=name, university=univ_obj)
        return Response({'message': 'Student created successfully'}, status=status.HTTP_201_CREATED)

class SubjectCreateView(APIView):
    parser_classes = [IsAuthenticated]


    def post(self, request):
        data = request.data
        name = data['name']
        prof = data['professor']
        univ = data['university']
        essential = data.get('essential', False)
        if Subject.objects.filter(name=name).exists():
            return Response({'message': 'Subject already exists'}, status=status.HTTP_400_BAD_REQUEST)
        if not Professor.objects.filter(name=prof).exists():
            return Response({'message': 'Professor does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        if not University.objects.filter(name=univ).exists():
            return Response({'message': 'University does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        univ_obj = University.objects.get(name=univ)
        prof_obj = Professor.objects.get(name=prof)
        subject = Subject.objects.create(name=name, professor=prof_obj, university=univ_obj, essential=essential)
        return Response({'message': 'Subject created successfully'}, status=status.HTTP_201_CREATED)
