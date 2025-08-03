\# SECURITY REVIEW



\## 🔐 1. HTTPS Configuration

\- \*\*Nginx\*\* is configured to redirect all HTTP traffic to HTTPS.

\- SSL/TLS is enabled using a self-signed certificate.

\- SSL protocols limited to TLSv1.2 and TLSv1.3 only.

\- Strong cipher suites configured.

\- Self-signed certificate generated with OpenSSL for testing purposes.



\## 🛡️ 2. Django Security Settings

\- `SECURE\_SSL\_REDIRECT = True`: Forces HTTPS requests.

\- `SECURE\_HSTS\_SECONDS = 31536000`: Enables HTTP Strict Transport Security (HSTS).

\- `SECURE\_HSTS\_INCLUDE\_SUBDOMAINS = True`

\- `SECURE\_HSTS\_PRELOAD = True`

\- `SESSION\_COOKIE\_SECURE = True`

\- `CSRF\_COOKIE\_SECURE = True`

\- `X\_FRAME\_OPTIONS = 'DENY'`: Protects against clickjacking.

\- `SECURE\_BROWSER\_XSS\_FILTER = True`

\- `SECURE\_CONTENT\_TYPE\_NOSNIFF = True`

\- `ALLOWED\_HOSTS` is set appropriately.



\## 🔒 3. Django User Management

\- Default user model replaced with a custom user model.

\- Passwords are hashed using Django's secure password hashers.

\- Admin access is restricted to staff users only.



\## 🧱 4. Access Control

\- Groups and permissions (view, create, edit, delete) implemented.

\- Permissions enforced at the view level using decorators and mixins.

\- Group-based access (Admin, Editor, Viewer) defined and applied.



\## 🔍 5. Input \& Output Security

\- Forms use CSRF protection.

\- User input is sanitized and validated via Django forms.

\- Output is automatically escaped by Django’s template engine (protects against XSS).



\## 📄 6. Logs and Monitoring

\- Nginx error logging enabled.

\- Django logs are managed and can be extended using Python’s logging module.



\## 🔁 7. Future Improvements

\- Replace self-signed cert with one from Let's Encrypt for production.

\- Set up Fail2ban or similar intrusion prevention.

\- Use environment variables for sensitive settings.



---



\*\*Reviewed by:\*\* Jackline Githinji 

\*\*Date:\*\* August 3, 2025  



