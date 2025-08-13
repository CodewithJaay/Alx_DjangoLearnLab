from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from .models import Book

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create users
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.staff_user = User.objects.create_user(username="staffuser", password="password123", is_staff=True)

        # Create token for authentication
        self.token = Token.objects.create(user=self.user)
        self.staff_token = Token.objects.create(user=self.staff_user)

        # Create sample books
        self.book1 = Book.objects.create(title="Book One", author="Author A")
        self.book2 = Book.objects.create(title="Book Two", author="Author B")

        # Endpoints
        self.list_url = "/api/books/"
        self.create_url = "/api/books/create/"
        self.update_url = f"/api/books/{self.book1.id}/update/"
        self.delete_url = f"/api/books/{self.book1.id}/delete/"
        self.detail_url = f"/api/books/{self.book1.id}/"

    def authenticate(self, token):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")

    def test_list_books(self):
        """Test retrieving list of books (no auth required)"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_book_detail(self):
        """Test retrieving a single book (no auth required)"""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.book1.title)

    def test_create_book_requires_authentication(self):
        """Test that creating a book without auth is forbidden"""
        response = self.client.post(self.create_url, {"title": "New Book", "author": "Author X"})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_book_authenticated(self):
        """Test that authenticated users can create a book"""
        self.authenticate(self.token)
        response = self.client.post(self.create_url, {"title": "New Book", "author": "Author X"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_update_book_requires_authentication(self):
        """Test that updating a book without auth is forbidden"""
        response = self.client.put(self.update_url, {"title": "Updated Book", "author": "Updated Author"})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_book_authenticated(self):
        """Test that authenticated users can update a book"""
        self.authenticate(self.token)
        response = self.client.put(self.update_url, {"title": "Updated Book", "author": "Updated Author"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book")

    def test_delete_book_requires_authentication(self):
        """Test that deleting a book without auth is forbidden"""
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_book_authenticated(self):
        """Test that authenticated users can delete a book"""
        self.authenticate(self.token)
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books_by_title(self):
        """Test filtering books by title"""
        response = self.client.get(self.list_url, {"search": "Book One"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(any(book["title"] == "Book One" for book in response.data))

    def test_order_books_by_title(self):
        """Test ordering books by title"""
        response = self.client.get(self.list_url, {"ordering": "title"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        titles = [book["title"] for book in response.data]
        self.assertEqual(titles, sorted(titles))
