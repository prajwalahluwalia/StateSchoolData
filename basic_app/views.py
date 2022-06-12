from audioop import reverse
from multiprocessing import context
from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from . import models
from basic_app.forms import StudentForm
from django.urls import reverse_lazy

# Create your views here.
# def index(request):
#     return render(request, 'basic_app/index.html')


class CBView(View):
    def get(self, request):
        return HttpResponse("CLASS VIEWS ARE COOL")

class IndexView(TemplateView):
    template_name = 'basic_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'Basic Injection for checking.'
        return context

class SchoolListView(ListView):

    context_object_name = 'schools'
    model = models.School
    #returns school_list as default name


class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School
    template_name = 'basic_app/school_detail.html'
    #returns school(model name in lowercase) as default name
    
#create school
class SchoolCreateView(CreateView):
    fields = ('name', 'principal', 'location')
    model = models.School

#update school
class SchoolUpdateView(UpdateView):
    fields = ('name', 'principal')
    model = models.School

#delete School
class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("basic_app:list")

#create Student
class StudentCreateView(CreateView):
    
    fields = ('name', 'age')
    model = models.Student

#update Student
class StudentUpdateView(UpdateView):
    fields = ('name', 'age')
    model = models.Student

class StudentDeleteView(DeleteView):
    model = models.Student
    success_url = reverse_lazy("basic_app:detail", kwargs={'pk':model.school})