from django.db import models

# Create your models here.
from django.db import models

# Author model represents a writer in the database
class Author(models.Model):
    name = models.CharField(max_length=255)  # Stores the author's full name

    def __str__(self):
        return self.name  # Shows the author's name in admin & shell


# Book model represents a book written by an author
class Book(models.Model):
    title = models.CharField(max_length=255)  # Book title
    publication_year = models.IntegerField()  # Year the book was published

    # ForeignKey creates a one-to-many relationship (1 author → many books)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,  # If author is deleted, delete their books
        related_name='books'       # Access books via author.books.all()
    )

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
