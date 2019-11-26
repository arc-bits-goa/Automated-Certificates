from django.shortcuts import render
from .models import *
from datetime import datetime,date
def printGraduating(request,id=None):

    instance = Graduating.objects.get(id=id)
    student = instance.student
    context = {
            "text"  :instance.text,
            "date"  :date.today(),
            "id"    :id,
            "student": student
    }
    return render(request,"print.html",context)

def printThesis(request,id=None):
	
    instance = Thesis.objects.get(id=id)
    context = {
            "text"  :instance.text,
            "date"  :date.today(),
            "id"    :id
    }
    return render(request,"print.html",context)

def printCGPA(request,id=None):
    
    instance = CGPAConversion.objects.get(id=id)
    context = {
            "text"  :instance.text,
            "date"  :date.today(),
            "id"    :id
    }
    return render(request,"print.html",context)

def printCompletion(request,id=None):
    
    instance = CourseCompletion.objects.get(id=id)
    context = {
            "text"  :instance.text,
            "date"  :date.today(),
            "id"    :id,
            "student": instance.student,
    }
    return render(request,"print.html",context)

def printEnglish(request,id=None):
    
    instance = English.objects.get(id=id)
    context = {
            "text"  :instance.text,
            "date"  :date.today(),
            "id"    :id
    }
    return render(request,"print.html",context)

def printContinuing(request,id=None):
    
    instance = Continuing.objects.get(id=id)
    context = {
            "text"  :instance.text,
            "date"  :date.today(),
            "id"    :id
    }
    return render(request,"print.html",context)

def printGraduated(request,id=None):
    
    instance = Graduated.objects.get(id=id)
    context = {
            "text"  :instance.text,
            "date"  :date.today(),
            "id"    :id
    }
    return render(request,"print.html",context)

def printSem(request,id=None):
    
    instance = ThesisSem.objects.get(id=id)
    context = {
            "text"  :instance.text,
            "date"  :date.today(),
            "id"    :id
    }
    return render(request,"print.html",context)
