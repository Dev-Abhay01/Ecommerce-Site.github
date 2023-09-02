from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=120)
    contact=models.CharField(max_length=20)
    message=models.CharField(max_length=600)

    def __str__(self):
        return self.name

class category(models.Model):
    cname=models.CharField(max_length=40)
    cimage=models.ImageField(upload_to='static/category/',default="")
    ADD_DATE=models.DateField()

    def __str__(self):
        return self.cname

class signup(models.Model):
    name=models.CharField(max_length=100)
    DOB=models.DateField()
    gender=models.CharField(max_length=20)
    Mobile=models.CharField(max_length=20)
    email=models.EmailField(max_length=80,primary_key=True)
    password=models.CharField(max_length=20)
    profession=models.CharField(max_length=150)
    working=models.CharField(max_length=80)
    profile_picture=models.ImageField(upload_to='static/profilepic/',default="")
    #RegDate=models.DateField()
    #Status=models.BooleanField()

    def __str__(self):
        return self.email

class blogdetail(models.Model):
    authorid=models.CharField(max_length=1000)
    blogcategory=models.CharField(max_length=100)
    btitle=models.TextField(max_length=90)
    bdescription=models.TextField()
    battachment=models.ImageField(upload_to='static/documents/',default="")
    bthumbnail=models.ImageField(upload_to='static/thumbnail/',default="")
    blogdate=models.DateField()

    def __str__(self):
        return self.authorid