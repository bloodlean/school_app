from django.urls import path, include
from .views import *

urlpatterns = [
    path('study_center/', study_center),
    path('study_detail/<int:pk>/', study_detail),
    path('teacher/', teacher),
    path('teacher_detail/<int:pk>/', teacher_detail),
    path('student/', student),
    path('student_detail/<int:pk>/', student_detail),

    path('auth/', include('dj_rest_auth.urls'))
]