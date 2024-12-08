
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


## Implementing Filtering, Searching and Ordering in Django REST Framework
Document the functionality in your project’s README or code comments:

Filtering: Users can filter by title, author, and publication_year. Use the query parameters title, author, or publication_year.
Searching: Users can search the title and author fields by using the search query parameter.
Ordering: Users can sort results by title or publication_year using the ordering parameter. Use a minus sign (-) for descending order.
Example API Requests:
Filter by author: /api/books/?author=John+Doe
Search for a book: /api/books/?search=python
Order by publication year descending: /api/books/?ordering=-publication_year



## Testing Strategy:

Unit Tests: These test the core functionality of each API endpoint, ensuring that CRUD operations work, that the filters and ordering function correctly, and that permissions are enforced.
Integration Tests: Ensure that the API integrates smoothly with the database and other parts of the application.
Authentication & Authorization: Ensure that only users with the proper roles (e.g., admin) can perform certain actions (e.g., delete).
Edge Cases: Test cases for invalid data, unauthorized access, and boundary conditions.
Test Cases:
test_create_book: Verifies that a book can be created by an authenticated user.
test_create_book_without_permission: Ensures that a non-authenticated user cannot create a book.
test_read_books: Verifies that all books can be retrieved.
test_update_book: Ensures that a book can be updated.
test_delete_book: Verifies that a book can be deleted.
test_permission_admin: Ensures that only admins can delete books.
test_filter_books: Verifies filtering by title works correctly.
test_order_books: Ensures that ordering by published date works as expected.