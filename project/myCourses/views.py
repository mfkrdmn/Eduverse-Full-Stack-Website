from django.views.generic import TemplateView
from django.shortcuts import render
from courses.models import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin # belli sayfalara login olmadan girememeyi ayarlar

    

class myCourses(LoginRequiredMixin, TemplateView):
    model = myCourses
    template_name = 'myCourses.html'
    context_object_name = "myCourses"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['myCourses'] = context['myCourses'].filter(user=self.request.user)

    #     return context
        # Bu yazdığımız fonkiyon ile farklı kullanıcıların 
        #verilerinin diğerinde gözükmesini önlüyoruz

def userDashboard(request):
    currentUser = request.user
    courses = currentUser.courses_joined.all()
    
    context = {
        "courses" : courses
    }

    return render(request,"myCourses.html", context)