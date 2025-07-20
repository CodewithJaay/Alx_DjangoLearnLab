from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Book

def list_books(request):
    books = Book.objects.all()
    output = '\n'.join([f"{book.title} by {book.author.name}" for book in books])
    return HttpResponse(output, content_type="text/plain")

from django.views.generic.detail import DetailView
from .models import Library

# Class-based view to display library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
