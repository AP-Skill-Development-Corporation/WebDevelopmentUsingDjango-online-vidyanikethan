from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hai(request):
	return HttpResponse("hai guys welcome django session")
def hello(request):
	return HttpResponse("<h3 style=color:skyblue;background-color:red;font-size:20px>goodmorning guys</h3>")

def hm(request):
	name="django project"
	return HttpResponse("this is my today"+name)
def sample(request,name):
	return HttpResponse('Enter your name:{}'.format(name))
def task(request,name,roll):
	print(name)
	print(roll)
	return HttpResponse("My name is{} and My roll nnumber is {}".format(name,roll))

def basic(request):
	return render(request,'myApp/basic.html')

def temp(request):
	return render(request,'myApp/temp.html')

def ls(request,name,id):
	return render(request,'myApp/ls.html',{'n':name,'i':id})

def table(request,num):
	data=[]
	for i in range(1,11):
		td=str(num)+"*"+str(i)+'='+str(num*i)
		data.append(td)
		print(td)

	return render(request,'myApp/table.html',{'info':data})

def table2(request):
	return render(request,'myApp/table2.html')
def inline(request):
	return render(request,'myApp/inline.html')
def external(request):
	return render(request,'myApp/external')