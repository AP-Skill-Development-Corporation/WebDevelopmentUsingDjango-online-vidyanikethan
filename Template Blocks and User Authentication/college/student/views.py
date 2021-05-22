from django.shortcuts import render, redirect
from django.http import HttpResponse
from student.models import Register,Library
from django.contrib import messages
from .forms import LibraryForm,UserForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from college.settings import LOGIN_URL

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


@login_required
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

def register(req):
    form = UserForm()
    if req.method=="POST":
        form = UserForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
            # return HttpResponse("Registrations Sucessful")
        else:
            return HttpResponse("Data is Invalid")
    return render(req,"s_register.html",{'form':form})


def signin(req):
    if req.method=="POST":
        uname = req.POST['uname']
        pswd = req.POST['pwd']
        user = authenticate(username=uname,password=pswd)
        if user is not None:
            login(req,user)
            return redirect('home')
        else:
            messages.error(req,"Username or Password is invalid ")
            return redirect('signin')

    return render(req,"signin.html")


@login_required
def signout(req):
    logout(req)
    return redirect('home')


@login_required
def profile(req):
    return render(req,"profile.html")
