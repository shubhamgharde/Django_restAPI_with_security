from django.shortcuts import render
from django_security.models import Employee
from django_security.serializer import EmployeeSerialization
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated,AllowAny


class EmployeeListOfOperations(ModelViewSet):
    #permission_classes = (AllowAny,)    #rest api ko security dena hai aur yaha bnd kana hai to ye line cooment out
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerialization


# from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly
#permission_classes = (AllowAny,)
