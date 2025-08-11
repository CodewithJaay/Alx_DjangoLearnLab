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
