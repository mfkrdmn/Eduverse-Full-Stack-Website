from django.shortcuts import render
from .models import *
# Create your views here.

def teachers(request):

    teachers = Teachers.objects.all()

    context = {
        "teachers": teachers,
    }

    return render(request, 'teachers.html', context)
    

