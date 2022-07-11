from audioop import reverse
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from courses.models import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
#class based yaklaşım


"""def index(request):
    return render(request, 'index.html')
"""
class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course'] = Courses.objects.filter(available=True).order_by('-date')[:4]
        context['teachers'] = Teachers.objects.filter(available=True)
        return context



"""def about(request):
    return render(request, 'about.html')"""

class AboutView(TemplateView):
    template_name = 'about.html'  


class ContactView(SuccessMessageMixin, FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')
    success_message = 'We received your request'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
