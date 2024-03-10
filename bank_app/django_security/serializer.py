from rest_framework.serializers import ModelSerializer
from django_security.models import Employee



class EmployeeSerialization(ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'