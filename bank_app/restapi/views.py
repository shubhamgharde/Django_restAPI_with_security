from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import *
from restapi.models import Book
from restapi.serializer import BookSerialization
from rest_framework.permissions import AllowAny,IsAdminUser,BasePermission



# A viewset that provides default create(), retrieve(), update(),
#partial_update(), destroy() and list() actions.

# class MyPermission(BasePermission):
#     # customize permission class---customize karne ke liye uska panrent class hona chaiy
#     def has_permission(self, request, view):
#         if request.action == 'create' and request.POST.get('author')=='manager':
#             return True     # agar action == manager hai to hi cahleaga
#         return True
#
#     def has_object_permission(self, request, view, obj):
#
#         return True

class BookOperations(ModelViewSet):   # all 6 --create --get-delete-put--patch
    permission_classes = (AllowAny,)  #AllowAny krna hai jab custome nahi banate hai
    queryset = Book.objects.all()
    serializer_class = BookSerialization


#  self.action agar uska destroy hota hai to peraticular book authenticated hota hai
    # books ke sare operation pubic hai except jo seft.action me likhenge
    #retrieve --user admin hoga to hi retrieve kr skta hai
    #create -- jab post method invoke karnege tb permission k liye

    def get_permissions(self):
        if self.action in ('retrieve',):
            self.permission_classes = [IsAdminUser,]
        return super(self.__class__, self).get_permissions()

'''  
class MyOwnViewset(CreateModelMixin, UpdateModelMixin):
    pass

class BookOperations(MyOwnViewset):  #all 6 -- create-put-patch
    queryset = Book.objects.all()
    serializer_class = BookSerialization
'''