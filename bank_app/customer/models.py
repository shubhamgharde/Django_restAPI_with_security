from django.db import models as db

# Create your models here.


class Customer(db.Model):
    name = db.CharField(max_length=30)
    email = db.EmailField(max_length=40, unique=True)
    dob = db.DateField()
    address = db.TextField(max_length=256)
    photo = db.FileField(upload_to='photos/')
    age = db.IntegerField()
    contact = db.BigIntegerField()

    class Meta:
        db_table = 'Customer_Master'
