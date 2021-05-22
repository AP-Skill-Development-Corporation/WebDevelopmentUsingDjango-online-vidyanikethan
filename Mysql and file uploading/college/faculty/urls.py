from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register, name='faculty_register'),
    path('data',views.disply_data, name='faculty_data')
]