from django.db.models import ForeignKey
from .models import Book, Author
from rest_framework import serializers

class Bookserializer (serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self,value):

        #Custom validation to check if the publication year is in the future.

        from datetime import date
        current_year = date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future")
        return value

class AuthorSerializer (serializers.ModelSerializer):

      #Serializer for the Author model.
     #Includes the 'name' field and a nested list of books for the related books.

    books = Bookserializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']