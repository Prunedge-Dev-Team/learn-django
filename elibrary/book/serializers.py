from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    author_details = serializers.SerializerMethodField('get_author_details')
    age = serializers.IntegerField(required=True, write_only=True)

    class Meta:
        model = Book
        fields = '__all__'
        extra_kwargs = {
            'author': {'write_only': True}
        }

    def validate(self, attrs):
        age = attrs.pop('age')
        if age < 18:
            raise ValidationError('This operation is for adult only', code=400)
        return attrs

    def get_author_details(self, obj):
        author = obj.author
        serializer = AuthorSerializer(author, many=False)
        return serializer.data
