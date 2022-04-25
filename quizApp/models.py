from django.conf import settings
from django.db import models

# Create your models here.

class AdminLogin(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    class Meta:
        db_table = "admin_login"


class Question(models.Model):
    question = models.CharField(max_length=500)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    correctAns = models.CharField(max_length=100)

    class Meta:
        db_table = "question"


class User(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    username_user = models.CharField(max_length=50)
    password_user = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    contact = models.CharField(max_length=50)
    image_url = models.FileField(upload_to='images')

    class Meta:
        db_table = "users"