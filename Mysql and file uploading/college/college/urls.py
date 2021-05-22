"""college URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from student import views as student_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',student_view.home,name='home'),
    path('student/register',student_view.student_register, name='student_register'),
    path('student/data',student_view.student_data,name='data'),
    path('student/update/<int:num>',student_view.student_update, name='update'),
    path('student/delete/<int:id>',student_view.student_delete,name='delete'),
    path('facutly/',include('faculty.urls')),
    path('student/library',student_view.library,name='library'),
]
