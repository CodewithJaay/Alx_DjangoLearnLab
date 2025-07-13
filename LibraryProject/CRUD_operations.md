# CRUD Operations Using Django Shell

This document shows how to perform Create, Retrieve, Update, and Delete operations using the Django shell with the `Book` model.

---

## Create a Book

```python
from bookshelf.models import Book

book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)

book = Book.objects.get(title="1984")
print(book.title)
print(book.author)
print(book.publication_year)

Output:
1984

book = Book.objects.get(title="1984")
print(book.title)
print(book.author)
print(book.publication_year)

Output:
1984
George Orwell
1949

book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)

Output:
Nineteen Eighty-Four

book.delete()
Book.objects.all()

Output:
(1, {'bookshelf.Book': 1})
<QuerySet []>
