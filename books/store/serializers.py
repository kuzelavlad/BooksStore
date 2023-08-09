from rest_framework import serializers
from rest_framework.response import Response
from .models import Books


# class UserSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = User
#         fields = ["id", "username", "password"]

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ["title", "author", "price", "date", "created_time", "modified_time", "status", "category"]

