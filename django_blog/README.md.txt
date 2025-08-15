# Django Blog – Authentication & Blog Post Management

## Overview
The `django_blog` project includes:
1. **User Authentication** – Register, log in, log out, and manage user profiles.
2. **Blog Post Management** – Create, Read, Update, and Delete (CRUD) blog posts.

---

## 1️⃣ Authentication System

### Features
- **Registration** – Users can sign up with a username, email, and password.
- **Login/Logout** – Users can log in to access protected features.
- **Profile Management** – Logged-in users can view and update their profile details.
- **Security** – All forms are protected with CSRF tokens, and passwords are securely hashed.

### URLs
| Path         | View               | Template                |
|--------------|--------------------|-------------------------|
| `/register/` | `register_view`    | `blog/register.html`     |
| `/login/`    | `LoginView`        | `blog/login.html`        |
| `/logout/`   | `LogoutView`       | `blog/logout.html`       |
| `/profile/`  | `profile_view`     | `blog/profile.html`      |

### Usage
1. **Register** – Go to `/register/`, fill in your details, and submit.
2. **Login** – Go to `/login/` and enter your credentials.
3. **Profile Update** – Go to `/profile/` to update email or other allowed fields.
4. **Logout** – Click the logout link to end your session.

---

## 2️⃣ Blog Post Management

### Features
- **List View** – View all blog posts with titles and content snippets.
- **Detail View** – View the full content of an individual post.
- **Create View** – Authenticated users can create new posts.
- **Update View** – Authors can edit their own posts.
- **Delete View** – Authors can delete their own posts.
- **Permissions** – Controlled access using Django’s `LoginRequiredMixin` and `UserPassesTestMixin`.

### URLs
| URL Path                  | View               | Description                           |
|---------------------------|--------------------|---------------------------------------|
| `/posts/`                 | PostListView       | List all blog posts                   |
| `/posts/new/`             | PostCreateView     | Create a new post (login required)    |
| `/posts/<int:pk>/`        | PostDetailView     | View a single post                    |
| `/posts/<int:pk>/edit/`   | PostUpdateView     | Edit a post (author only)             |
| `/posts/<int:pk>/delete/` | PostDeleteView     | Delete a post (author only)           |

### Usage
1. **View Posts** – Visit `/posts/` to see all posts.
2. **View a Post** – Click a post title to view its details.
3. **Create a Post** – Log in, go to `/posts/new/`, fill in the form, and submit.
4. **Edit/Delete** – Only the author of a post can edit or delete it.

---

## Security Notes
- All forms include `{% csrf_token %}` to protect against CSRF attacks.
- Passwords are stored using Django’s built-in hashing.
- Access control:
  - **Authenticated users**: Can create posts.
  - **Post authors**: Can edit or delete their own posts.
  - **Anyone**: Can view posts.

---

## Testing Instructions
1. **Authentication**
   - Register a new account.
   - Log out and log in again.
   - Update profile details and confirm changes are saved.

2. **Blog Post Management**
   - Create posts as different users.
   - Confirm only authors can edit/delete their own posts.
   - Ensure list and detail pages are accessible without login.

---

## Future Improvements
- Add profile pictures and bios to user profiles.
- Implement email verification for new accounts.
- Add categories/tags for blog posts.
- Enable pagination for post lists.
- Add a search feature for posts.
