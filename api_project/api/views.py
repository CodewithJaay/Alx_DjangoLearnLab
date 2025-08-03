"""
Authentication:
- Token-based authentication using DRF's TokenAuthentication.
- Token obtained via /api/auth/token/ with username & password.

Permissions:
- All BookViewSet actions require authentication.
- Change to IsAdminUser or custom permissions if needed.
"""


from django.shortcuts import render

# Create your views here.

from rest_framework import generics, viewsets, permissions
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# New ViewSet for full CRUD
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]