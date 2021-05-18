from django.db import models

class Register(models.Model):
    Faculty_name = models.CharField(max_length=10)
    Faculty_mail = models.EmailField()
    Faculty_age = models.IntegerField()
    Faculty_phone = models.CharField(max_length=10)

    def __str__(self):
        return self.Faculty_name
