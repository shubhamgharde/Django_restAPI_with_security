from django.db import models
from django.db.models.signals import *     #singnlling ke liye
from django.dispatch import receiver       #singnlling ke liye


from django.db.models.signals import post_delete      #singnlling ke liye


class Employee(models.Model):
    name =models.CharField(max_length=30)
    age = models.IntegerField()
    role = models.CharField(max_length=30)
    email = models.EmailField()

    class Meta:
        db_table = "EMPLOYEE_INFO"


#ye niche wala code signalling ke liye
@receiver(post_save, sender=Employee)
def after_role_changed(sender, instance, created, raw, using, update_fields,*args,**kwargs):
    print('--'*40)
    print(sender, instance, created, raw, using, update_fields)
    print('after_role_changed -- method called')
    #send email   #yaha agar send email ka code rkhe to auto code bhejega
    print('--'*40)


@receiver(post_delete, sender=Employee)
def after_employee_delete(sender, instance, using,*args,**kwargs):
    print('--'*40)
    print(sender, instance, using)
    print('after_employee_delete -- method called')
    #send email   #yaha agar send email ka code rkhe to auto code bhejega
    print('--'*40)
