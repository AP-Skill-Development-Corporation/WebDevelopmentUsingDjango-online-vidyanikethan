from django.forms import ModelForm
from .models import Register


class FacultyRegisterForm(ModelForm):
    class Meta:
        model = Register
        fields = "__all__"