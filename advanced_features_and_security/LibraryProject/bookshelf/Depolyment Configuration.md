# Enforce HTTPS redirection for all non-HTTPS requests
SECURE_SSL_REDIRECT = True

# Enable HTTP Strict Transport Security (HSTS) with a 1-year duration
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Ensure cookies are only sent over secure connections
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Implement secure HTTP headers
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True