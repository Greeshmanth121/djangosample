from django.shortcuts import render
from .models import student

def home(request):
    return render(request,'home.html')

def addstudent(request):
    if request.method == 'POST':
        sname = request.POST['sname']
        course = request.POST['course']
        fees = request.POST['fees']
        st = student(sname=sname,course=course,fees=fees)
        st.save()
        return render(request,'add_student.html',{'saved':True})

    return render(request,'add_student.html')
