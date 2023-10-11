from django.db import models

# Create your models here.
class Booking(models.Model):
    referal_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    city=models.CharField(max_length=20,default="london")
    issue=models.TextField()
    description=models.CharField(max_length=200)
    citizenship_id=models.CharField(max_length=16)
    relation=models.CharField(max_length=50)

class SignUp(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=20)
    phone_number=models.CharField(max_length=12)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    confirm_password=models.CharField(max_length=50)

# class login(models.Model):
#     email_address=models.CharField(max_length=50)
#     login_password=models.CharField(max_length=50)
# class Employee(models.Model):
#     name=models.CharField(max_length=100)
#     email=models.CharField(max_length=50)
#     address=models.CharField(max_length=200)
#     phone=models.CharField(max_length=10)
#     about=models.TextField()
#     company=models.ForeignKey(Company,on_delete=models.CASCADE)