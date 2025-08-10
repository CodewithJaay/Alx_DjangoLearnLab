from rest_framework import serializers
from django.utils import timezone
from .models import Author, Book


class BookSerializer(serializers.ModelSerializer):
    """
    Serializes Book model data.
    Includes custom validation to ensure publication_year is not in the future.
    """

    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        """
        Custom validation method.
        Ensures that the publication year is not greater than the current year.
        """
        current_year = timezone.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializes Author model data.
    Includes a nested serializer to list all books related to the author.
    """
    books = BookSerializer(many=True, read_only=True)
    # 'books' comes from related_name='books' in the Book model.

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
