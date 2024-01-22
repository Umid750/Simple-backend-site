from django.shortcuts import render
from .models import *
from .form import *
from django.http import HttpResponse

# Create your views here.

def home(request):
    student = Student.objects.all()
    context = {
        'student':student
    }
    return render(request, 'index.html', context)

def studentform(request):
    if request.method == 'STUDENT':
        form = StudentForm(request.STUDENT)
        if form.is_valid():
            form.save()
            return HttpResponse(f"Form saved!")
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form':form})