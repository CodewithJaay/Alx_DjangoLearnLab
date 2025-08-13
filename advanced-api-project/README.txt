# Advanced API Project - Generic Views
This project uses Django REST Framework's generic views for efficient CRUD.

## Endpoints:
- GET /api/books/ → List all books (public)
- GET /api/books/<id>/ → Retrieve book (public)
- POST /api/books/create/ → Create book (auth only)
- PUT/PATCH /api/books/<id>/update/ → Update book (auth only)
- DELETE /api/books/<id>/delete/ → Delete book (auth only)

## Permissions:
- Read: public
- Create/Update/Delete: authenticated users only

## Testing:
Use Postman or curl commands in the docs.

---

## Book API — Advanced Query Features

This API supports **filtering**, **searching**, and **ordering** for books.

### Filtering
Filter by exact matches on:
- `title`
- `author` (use author ID)
- `publication_year`

**Examples:**
```
/api/books/?title=Python%20Basics
/api/books/?author=1
/api/books/?publication_year=2020
```

---

### Searching
Search text in:
- `title`
- `author__name` (searches author name directly)

**Examples:**
```
/api/books/?search=Harry
/api/books/?search=John%20Doe
```

---

### Ordering
Order results by:
- `title`
- `publication_year`

**Examples:**
```
/api/books/?ordering=title
/api/books/?ordering=-publication_year
```
(`-` before a field means descending order.)

---

### Combining Queries
You can mix filtering, searching, and ordering in the same request.

**Example:**
```
/api/books/?author=1&search=Python&ordering=-publication_year
```

---

**Note:**  
- Filtering is case-sensitive for exact matches.  
- Searching is case-insensitive and matches partial words.
