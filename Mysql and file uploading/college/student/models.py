from django.db import models

# Create your models here.
class Register(models.Model):
    Student_name = models.CharField(max_length=10)
    Email = models.EmailField()
    Branch = models.CharField(max_length=5)
    gender_list = [('Male','Male'),('Female','Female')]
    gender = models.CharField(choices=gender_list, max_length=7,null=True, blank='True')
    age = models.IntegerField(null=True, blank='True')
    dob = models.DateField(null=True,blank=True)

    def __str__(self):
        return self.Student_name


class Library(models.Model):
	book_id  = models.IntegerField()
	book_name = models.CharField(max_length=50)
	book_author = models.CharField(max_length=30)
	publication_date = models.DateField()
	image = models.ImageField(upload_to='library/')


	def __str__(self):
		return self.book_name