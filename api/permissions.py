from rest_framework.permissions import BasePermission


#STUDY_CENTER PERMISSIONS

class Study_centerPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        elif request.method == 'POST':
            return request.user.is_staff

class StudyDetailPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True 
        elif request.method in ['PUT', 'DELETE']:
            return request.user.is_staff

#TEACHER PERMISSIONS

class TeacherPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        elif request.method == 'POST':
            return request.user.is_staff

class TeacherDetailPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        elif request.method in ['PUT', 'DELETE']:
            return request.user.is_staff

#STUDENT PERMISSIONS

class StudentPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.user.is_staff
        elif request.method == 'POST':
            return request.user.is_staff

class StudentDetailPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return request.user.is_staff
        elif request.method in ['PUT', 'DELETE']:
            return request.user.is_staff