from  rest_framework.serializers import ModelSerializer,HyperlinkedModelSerializer
from restapi.models import Book

class BookSerialization(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'                #sab fields serialize hinge
        #fields = ('id','name', 'price')  # sirf itne hi serialize honge baki deserialize honge
        #exclude = ('id','name','price')  #inko chod k baki sab serialize honge