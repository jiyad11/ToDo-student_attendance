from django.shortcuts import render, redirect

from myapp1.forms import student_form
from myapp1.models import student_task


# Create your views here.
def index(request):
    return render(request,'index.html')

def add_student(request):
    form = student_form()
    if request.method == 'POST':
        form = student_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_student')
    return render(request,'add_student.html',{'form' : form})

def view_student(request):
    details = student_task.objects.all()
    return render(request,'view_student.html',{'details' : details})

def update_student(request,id):
    details = student_task.objects.get(id=id)
    form = student_form(instance=details)
    if request.method == 'POST':
        form = student_form(request.POST or None, instance=details or None)
        if form.is_valid():
            form.save()
            return redirect('view_student')
    return render(request,'edit_student.html',{'form' : form})

def delete_student(request,id):
    details = student_task.objects.get(id=id)
    form = student_form(instance=details)
    details.delete()
    return redirect('view_student')