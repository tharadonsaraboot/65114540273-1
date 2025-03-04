from django.shortcuts import render, redirect
from .models import Course
from django.http import HttpResponse

def add_course(request):
    if request.method == "POST":
        code = request.POST.get('code')
        name = request.POST.get('name')
        credit = request.POST.get('credit')
        
        Course.objects.create(code=code, name=name, credit=credit)
        return redirect('list_courses')
    
    return render(request, 'courses/add_course.html')

def list_courses(request):
    courses = Course.objects.all()
    return render(request, 'courses/list_courses.html', {'courses': courses})