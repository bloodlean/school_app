from django.urls import path, include
from .views import *

urlpatterns = [
    path('study_center/', study_center),
    path('study_detail/<pk>/', study_detail),
    path('teacher/', teacher),
    path('teacher_detail/<pk>/', teacher_detail),
    path('student/', student),
    path('student_detail/<pk>/', student_detail),

    path('auth/', include('dj_rest_auth.urls'))
]