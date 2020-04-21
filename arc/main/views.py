from django.shortcuts import render
from .models import *
from datetime import datetime,date
def refSemester():
    
    year = date.today().year%2000
    semtext = ("II/"+str(year-1)+"-"+str(year)) if date.today().month<7 else ("I/"+str(year)+"-"+str(year+1))
    return semtext

def dateText():
    dtext = datetime.now().strftime("%B")+" "+str(date.today().day)+", "+str(date.today().year)
    return dtext

def printGraduating(request,id=None):

    instance = Graduating.objects.get(id=id)
    student = instance.student
    context = {
            "text"  :instance.text,
            "date"  :dateText(),
            "id"    :id,
            "student": student,
            "reftext": refSemester()
    }
    return render(request,"print.html",context)

def printThesis(request,id=None):
	
    instance = Thesis.objects.get(id=id)
    context = {
            "student":instance.student,
            "text"  :instance.text,
            "date"  :dateText(),
            "id"    :id,
            "reftext": refSemester()
    }
    return render(request,"print.html",context)

def printCGPA(request,id=None):
    
    instance = CGPAConversion.objects.get(id=id)
    context = {
            "student":instance.student,
            "text"  :instance.text,
            "date"  :dateText(),
            "id"    :id,
            "reftext": refSemester()
    }
    return render(request,"print.html",context)

def printCompletion(request,id=None):
    
    instance = CourseCompletion.objects.get(id=id)
    context = {
            "student":instance.student,
            "text"  :instance.text,
            "date"  :dateText(),
            "id"    :id,
            "reftext": refSemester()
    }
    return render(request,"print.html",context)

def printEnglish(request,id=None):
    
    instance = English.objects.get(id=id)
    context = {
            "student":instance.student,
            "text"  :instance.text,
            "date"  :dateText(),
            "id"    :id,
            "reftext": refSemester()
    }
    return render(request,"print.html",context)

def printContinuing(request,id=None):
    
    instance = Continuing.objects.get(id=id)
    context = {
            "student":instance.student,
            "text"  :instance.text,
            "date"  :dateText(),
            "id"    :id,
            "reftext": refSemester()
    }
    return render(request,"print.html",context)

def printGraduated(request,id=None):
    
    instance = Graduated.objects.get(id=id)
    context = {
            "student":instance.student,
            "text"  :instance.text,
            "date"  :dateText(),
            "id"    :id,
            "reftext": refSemester()
    }
    return render(request,"print.html",context)

def printSem(request,id=None):
    
    instance = ThesisSem.objects.get(id=id)
    context = {
            "student":instance.student,
            "text"  :instance.text,
            "date"  :dateText(),
            "id"    :id,
            "reftext": refSemester()
    }
    return render(request,"print.html",context)
