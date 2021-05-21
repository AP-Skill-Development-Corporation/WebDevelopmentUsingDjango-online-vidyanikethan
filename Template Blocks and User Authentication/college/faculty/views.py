from django.shortcuts import render
from django.http import HttpResponse
from .forms import FacultyRegisterForm
from .models import Register


def register(request):
    form = FacultyRegisterForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponse('FacultyRegisterForm post method')
        return HttpResponse("form is not valid")
    return render(request,'register.html',{'form':form})

def disply_data(requst):
    data = Register.objects.all()
    return render(requst, 'disply.html',{'data':data})
