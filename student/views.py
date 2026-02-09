from django.shortcuts import render
from .models import Student

def home(request):
    return render(request, 'student/home.html')

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student/student_list.html', {'students': students})
