from .views import *
from django.urls import path


urlpatterns = [

    path('school/', manage_school),
    path('school/<int:id>/', manage_school),

    path('grade/', manage_grade),
    path('grade/<int:id>/', manage_grade),


    path('students/', manage_student),
    path('students/<int:id>/', manage_student),


    path('teacher/', manage_teacher),
    path('teacher/<int:id>/', manage_teacher),

    path('subjects/', manage_subjects),
    path('subjects/<int:id>/', manage_subjects),



]