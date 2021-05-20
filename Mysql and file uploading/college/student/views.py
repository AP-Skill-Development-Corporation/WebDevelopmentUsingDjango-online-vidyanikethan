from django.shortcuts import render, redirect
from django.http import HttpResponse
from student.models import Register,Library
from django.contrib import messages
from .forms import LibraryForm
# Create your views here.

def student_register(request):
    if request.method == 'POST':
        name = request.POST['Name']
        email = request.POST['Email']
        branch = request.POST['Branch']
        age = request.POST['Age']
        dob = request.POST['Dob']
        gender = request.POST['gender']
        new_data= Register(Student_name=name, Branch= branch, Email=email,
                           age=age, dob=dob, gender=gender)
        new_data.save()
        return redirect('data')
    return render(request,'student register.html')


def student_data(request):
    data = Register.objects.all()
    return render(request, 'result.html', {'context': data})

def student_update(request, num):
    single_row = Register.objects.get(id=num)
    if request.method == 'POST':
        single_row.Student_name = request.POST.get('Name')
        single_row.Branch = request.POST.get('Branch')
        single_row.Email = request.POST['Email']
        single_row.age = request.POST['Age']
        single_row.dob = request.POST['Dob']
        single_row.gender = request.POST['gender']
        single_row.save()
        return redirect('data')
    return render(request,'update.html',{'data':single_row})

def student_delete(request,id):
    details = Register.objects.get(id=id)
    name = details.Student_name
    details.delete()
    messages.success(request, ' Details Deleted')
    return redirect('data')



def library(request):
    form = LibraryForm()
    if request.method=='POST':
        form = LibraryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            return HttpResponse("The data is invalid")
    return render(request,'library.html',{'form':form})


def home(request):
    return render(request,'home.html')
