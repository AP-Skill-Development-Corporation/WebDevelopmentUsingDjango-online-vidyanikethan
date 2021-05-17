from django.shortcuts import render, redirect
from django.http import HttpResponse
from student.models import Register


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
    return render(request,'update.html',{'data':single_row})