from django.shortcuts import render, redirect
from .forms import StudentForm, SubjectForm
from .models import Student, Subject
from django.contrib.auth.decorators import login_required


@login_required(login_url='login_url')
def add_stu_view(request):
    form = StudentForm()
    if request.method=="POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_sub_url')
    template_name = 'stu_app/student_form.html'
    context = {'form':form}
    return render(request, template_name, context)

@login_required(login_url='login_url')
def add_sub_view(request):
    form = SubjectForm()
    if request.method=="POST":
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_sub_url')
    template_name = 'stu_app/subject_form.html'
    context = {'form':form}
    return render(request, template_name, context)

@login_required(login_url='login_url')
def show_stu_view(request):
    data = Student.objects.all()
    template_name = 'stu_app/show_student.html'
    context = {'data':data}
    return render(request, template_name, context)

@login_required(login_url='login_url')
def show_sub_view(request):
    data = Subject.objects.all()
    template_name = 'stu_app/show_subject.html'
    context = {'data':data}
    return render(request, template_name, context)

def update_stu_view(request,pk):
    obj = Student.objects.get(id=pk)
    form = StudentForm(instance=obj)
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_stu_url')
    template_name = 'stu_app/update_student.html'
    context = {'form':form}
    return render(request, template_name, context)

def update_sub_view(request,pk):
    obj = Subject.objects.get(id=pk)
    form = SubjectForm(instance=obj)
    if request.method == "POST":
        form = SubjectForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_sub_url')
    template_name = 'stu_app/update_subject.html'
    context = {'form':form}
    return render(request, template_name, context)

def delete_stu_view(request,pk):
    obj = Student.objects.get(id=pk)
    if request.method == "POST":
        obj.delete()
        return redirect('show_stu_url')

    template_name = 'stu_app/delete_student.html'
    context = {'data':obj}
    return render(request,template_name,context)


def delete_sub_view(request,pk):
    obj = Subject.objects.get(id=pk)
    if request.method == "POST":
        obj.delete()
        return redirect('show_sub_url')

    template_name = 'stu_app/delete_subject.html'
    context = {'data':obj}
    return render(request,template_name,context)


