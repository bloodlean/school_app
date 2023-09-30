from rest_framework import serializers
from app.models import *

class Study_centerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Study_center
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'