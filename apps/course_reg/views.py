from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Course

def index(request):
    course_list = Course.objects.all()
    context = {
        'courses': course_list
    }
    return render(request, "course_reg/index.html", context)

def process(request):
    Course.objects.validate(request)
    return redirect("/")

def destroy(request, id):
    course_list = Course.objects.filter(id=id)
    context = {
        'courses': course_list
    }
    return render(request, "course_reg/destroy.html", context)

def delete(request, id):
    Course.objects.delete(request, id)
    return redirect("/")