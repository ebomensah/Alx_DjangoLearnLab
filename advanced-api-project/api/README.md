
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
