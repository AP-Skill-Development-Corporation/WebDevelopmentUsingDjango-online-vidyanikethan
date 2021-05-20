from django.shortcuts import render
from django.http import HttpResponse
from .forms import registerationForm

from django.core.mail import send_mail
from Mailsending import settings
# Create your views here.


def register(request):
	form = registerationForm()
	if request.method=='POST':
		form = registerationForm(request.POST)
		form.save()
		sub = "sucess"
		body = "Hello!"+ form.cleaned_data['name'] + "Your registration is successful"
		from_id = settings.EMAIL_HOST_USER
		to_id = form.cleaned_data['email']
		# print(to_id)
		send_mail(sub,body,from_id,[to_id])
		return HttpResponse("Registration Successful and Check your mail !")
	return render(request,"register.html",{'form':form})