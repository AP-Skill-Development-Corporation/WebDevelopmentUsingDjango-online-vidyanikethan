from django.db import models

# Create your models here.
class register(models.Model):
	name = models.CharField(max_length=20)
	email = models.EmailField()
	phone = models.CharField(max_length=10)
