from django.db import models

# Create your models here.


class Book(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    qyt = models.IntegerField()
    publication = models.CharField(max_length=30)
    author = models.CharField(max_length=30)

    class Meta:
        db_table = "BOOK_MASTER"

    def __str__(self):
        return f'''{self.__dict__}'''

    def __repr__(self):
        return str(self)
