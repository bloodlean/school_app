from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.status import *
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser
from .permissions import *

from app.models import Study_center
from .serializers import Study_centerSerializer
from app.models import Teacher
from .serializers import TeacherSerializer
from app.models import Student
from .serializers import StudentSerializer

@api_view(['GET', 'POST'])
@permission_classes([Study_centerPermission])
def study_center(request):

    if request.method == 'GET':
        events = Study_center.objects.all()
        serializer = Study_centerSerializer(events, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

@api_view(['GET', 'POST'])
@permission_classes([StudyDetailPermission])
def study_detail(request, pk):

    study_center = Study_center.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = Study_centerSerializer(Study_center)
        return Response(serializer.data, status=HTTP_202_ACCEPTED) 
    elif request.method == 'POST':
        serializer = Study_centerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)     
    elif request.method == 'PUT':
        serializer = Study_centerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        study_center.delete()
        return Response(status=HTTP_204_NO_CONTENT)

    
#TEACHER
@api_view(['GET', 'POST'])
@permission_classes([TeacherPermission])
def teacher(request):

    if request.method == 'GET':
        teacher = Teacher.objects.all()
        serializer = TeacherSerializer(teacher, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

@api_view(['GET', 'POST'])
@permission_classes([TeacherDetailPermission])
def teacher_detail(request, pk):

    teacher = Teacher.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = TeacherSerializer(Teacher)
        return Response(serializer.data, status=HTTP_202_ACCEPTED) 
    elif request.method == 'POST':
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)     
    elif request.method == 'PUT':
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        teacher.delete()
        return Response(status=HTTP_204_NO_CONTENT)

#STUDENTS
@api_view(['GET', 'POST'])
@permission_classes([StudentPermission])
def student(request):

    if request.method == 'GET':
        student = Student.objects.all()
        serializer = StudentSerializer(student, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

@api_view(['GET', 'POST'])
@permission_classes([StudentDetailPermission])
def student_detail(request, pk):

    student = Student.objects.get(pk=pk)

    if request.method == 'GET':
        serializer = StudentSerializer(Student)
        return Response(serializer.data, status=HTTP_202_ACCEPTED) 
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)     
    elif request.method == 'PUT':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=HTTP_204_NO_CONTENT)
