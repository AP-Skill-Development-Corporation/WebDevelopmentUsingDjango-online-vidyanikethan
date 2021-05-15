from django.shortcuts import render
from django.http import HttpResponse
from student.models import Register


# Create your views here.

def student_register(request):
    if request.method == 'POST':
        name = request.POST['Name']
        email = request.POST['Email']
        branch = request.POST['Branch']
        new_data= Register(Student_name=name, Branch= branch, Email=email)
        new_data.save()
        return render(request,'result.html',{'name':name, 'email':email,
                                             'branch':branch})
    return render(request,'student register.html')