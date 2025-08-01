# LibraryProject

This is a beginner Django project created to explore Django’s project structure and understand its core components.

## Permissions & Groups Setup

This app uses Django's permissions system to manage access:

### Custom Permissions:

Defined in the `Book` model (`bookshelf/models.py`):

- `can_view` — View articles
- `can_create` — Create new articles
- `can_edit` — Edit articles
- `can_delete` — Delete articles

These permissions are added using the `Meta.permissions` attribute.

### Groups:

Three user groups are defined to structure access:

- **Viewers**: can_view
- **Editors**: can_view, can_create, can_edit
- **Admins**: can_view, can_create, can_edit, can_delete

Each group corresponds to specific actions users can perform on `Book` objects.

### Setup

After running migrations and creating your superuser, run the following command to auto-create the groups and assign permissions:


```bash
python manage.py setup_groups
