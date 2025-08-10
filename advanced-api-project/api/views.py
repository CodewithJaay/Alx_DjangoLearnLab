from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Authors.
    Includes all CRUD operations and nested books via the AuthorSerializer.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing Books.
    Includes all CRUD operations with validation from BookSerializer.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
