from django.db import models

# Create your models here.
class Register(models.Model):
    Student_name = models.CharField(max_length=10)
    Email = models.EmailField()
    Branch = models.CharField(max_length=5)

    def __str__(self):
        return self.Student_name