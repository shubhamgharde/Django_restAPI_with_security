from rest_framework.routers import SimpleRouter
from django_security.views import EmployeeListOfOperations
simple = SimpleRouter()
simple.register('api/v1',EmployeeListOfOperations)
urlpatterns = simple.urls
