from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
# from rest_framework.decorators import action
# from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Books
from .serializers import BooksSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    permission_classes = [IsAuthenticated]
    filterset_fields = ['price', 'date', 'status', 'category']
    search_fields = ['name', 'author', 'status', 'category']
    ordering_fields = ['price', 'author', 'status', 'category']

def auth(request):
    return render(request, 'oauth.html')