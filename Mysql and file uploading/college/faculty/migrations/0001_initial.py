# Generated by Django 3.0.7 on 2021-05-18 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Faculty_name', models.CharField(max_length=10)),
                ('Faculty_mail', models.EmailField(max_length=254)),
                ('Faculty_age', models.IntegerField()),
                ('Faculty_phone', models.CharField(max_length=10)),
            ],
        ),
    ]
