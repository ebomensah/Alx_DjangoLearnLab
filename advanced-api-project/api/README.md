
## Book API Views Documentation

### Endpoints:

- **GET /books/**: Retrieve a list of all books.
- **GET /books/<int:pk>/**: Retrieve a single book by ID.
- **POST /books/create/**: Create a new book (Authenticated users only).
- **PUT /books/<int:pk>/update/**: Update an existing book (Authenticated users only).
- **DELETE /books/<int:pk>/delete/**: Delete a book by ID (Authenticated users only).

### Authentication:
- **Create, Update, and Delete Views**: Require authentication via token or session.
- **List and Detail Views**: Accessible to all users, no authentication required.


# Create your tests here.
