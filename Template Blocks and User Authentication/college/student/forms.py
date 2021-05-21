from django import forms
from .models import Library
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class LibraryForm(forms.ModelForm):
	class Meta:
		model = Library
		fields = "__all__"

		widgets = {
		'book_id': forms.NumberInput(attrs = {'class':'form-control'}),
		'book_name': forms.TextInput(attrs = {'class':'form-control'}),
		'book_author': forms.TextInput(attrs = {'class':'form-control'}),
		'publication_date':forms.DateInput(attrs = {'class':'form-control'}),

		}


class UserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['first_name',"last_name","email","username","password1","password2"]