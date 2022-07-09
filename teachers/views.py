from django.shortcuts import render
from .models import *
# Create your views here.

def teachers(request):

    teachers = Teachers.objects.all()

    context = {
        "teachers": teachers,
    }

    return render(request, 'teachers.html', context)
    

def teacher_details(request):
    
    course_teachers = Teachers.objects.all()

    context = {
        "course_teachers" : course_teachers,
    }

    return render(request, 'course.html', context)