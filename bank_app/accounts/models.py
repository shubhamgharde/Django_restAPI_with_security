from django.db import models

# Create your models here.


#customer- account  : 1-1
#bank    - account  : 1-m   many side foreign key
#customer- bank     : m-1
#customer- address  : m-m


class Cust(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    bank = models.ForeignKey('Bank', on_delete=models.CASCADE)
    class Meta:
        db_table = "CUST_MASTER"


class Address(models.Model):
    city = models.CharField(max_length=30)
    pincode = models.IntegerField()
    bank = models.ManyToManyField(Cust)
    class Meta:
        db_table = "ADDRESS _MASTER"


class Account(models.Model):
    type = models.CharField(max_length=30)
    balance = models.FloatField()
    customer = models.OneToOneField(Cust, on_delete=models.CASCADE)
    bank = models.ForeignKey('Bank', on_delete=models.CASCADE)
    class Meta:
        db_table = "ACCOUNT_MASTER"


class Bank(models.Model):
    name = models.CharField(max_length=30)
    ifscode = models.CharField(max_length=30)

    class Meta:
        db_table = "BANK_MASTER"
