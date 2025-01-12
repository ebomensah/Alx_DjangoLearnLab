1. Test POST /api/posts/ (Create a Post)
Request:

Method: POST
URL: http://localhost:8000/api/posts/
Headers:
Authorization: Token <valid_user_token>
Body (JSON):
json
Copy code
{
  "title": "First Post",
  "content": "This is the content of the first post."
}
Response:

Status Code: 201 Created
Body:
json
Copy code
{
  "id": 1,
  "author": 1,
  "title": "First Post",
  "content": "This is the content of the first post.",
  "created_at": "2025-01-12T12:34:56Z",
  "updated_at": "2025-01-12T12:34:56Z"
}
Notes:

The post is successfully created with the authenticated user as the author.
The created_at and updated_at timestamps are automatically assigned.
2. Test GET /api/posts/ (Retrieve List of Posts with Pagination)
Request:

Method: GET
URL: http://localhost:8000/api/posts/
Headers:
Authorization: Token <valid_user_token>
Response:

Status Code: 200 OK
Body:
json
Copy code
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "author": 1,
      "title": "First Post",
      "content": "This is the content of the first post.",
      "created_at": "2025-01-12T12:34:56Z",
      "updated_at": "2025-01-12T12:34:56Z"
    }
  ]
}
Notes:

Only one post is available, and pagination is working as expected (count, next, and previous fields).
The results are displayed with the correct pagination setup (PAGE_SIZE of 10).
3. Test GET /api/posts/?search=First (Search for Posts by Title)
Request:

Method: GET
URL: http://localhost:8000/api/posts/?search=First
Headers:
Authorization: Token <valid_user_token>
Response:

Status Code: 200 OK
Body:
json
Copy code
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "author": 1,
      "title": "First Post",
      "content": "This is the content of the first post.",
      "created_at": "2025-01-12T12:34:56Z",
      "updated_at": "2025-01-12T12:34:56Z"
    }
  ]
}
Notes:

The search functionality works as expected, filtering the posts by the term "First" in the title.
4. Test POST /api/comments/ (Create a Comment on a Post)
Request:

Method: POST
URL: http://localhost:8000/api/comments/
Headers:
Authorization: Token <valid_user_token>
Body (JSON):
json
Copy code
{
  "post": 1,
  "content": "Great post!"
}
Response:

Status Code: 201 Created
Body:
json
Copy code
{
  "id": 1,
  "author": 1,
  "post": 1,
  "content": "Great post!",
  "created_at": "2025-01-12T12:35:00Z",
  "updated_at": "2025-01-12T12:35:00Z"
}
Notes:

The comment is successfully created with the authenticated user as the author, associated with the post (ID: 1).
The created_at and updated_at timestamps are automatically assigned.
5. Test GET /api/comments/?post=1 (Retrieve Comments for a Specific Post)
Request:

Method: GET
URL: http://localhost:8000/api/comments/?post=1
Headers:
Authorization: Token <valid_user_token>
Response:

Status Code: 200 OK
Body:
json
Copy code
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "author": 1,
      "post": 1,
      "content": "Great post!",
      "created_at": "2025-01-12T12:35:00Z",
      "updated_at": "2025-01-12T12:35:00Z"
    }
  ]
}
Notes:

The comment related to post ID 1 is retrieved successfully.
6. Test PUT /api/posts/{id}/ (Update a Post)
Request:

Method: PUT
URL: http://localhost:8000/api/posts/1/
Headers:
Authorization: Token <valid_user_token>
Body (JSON):
json
Copy code
{
  "title": "Updated Post Title",
  "content": "Updated content for the post."
}
Response:

Status Code: 200 OK
Body:
json
Copy code
{
  "id": 1,
  "author": 1,
  "title": "Updated Post Title",
  "content": "Updated content for the post.",
  "created_at": "2025-01-12T12:34:56Z",
  "updated_at": "2025-01-12T12:45:00Z"
}
Notes:

The post is successfully updated with the new title and content.
The updated_at timestamp reflects the change.
7. Test DELETE /api/posts/{id}/ (Delete a Post)
Request:

Method: DELETE
URL: http://localhost:8000/api/posts/1/
Headers:
Authorization: Token <valid_user_token>
Response:

Status Code: 204 No Content
Body: Empty body (successful deletion)
Notes:

The post is successfully deleted.
The response body is empty, as expected for a successful DELETE request.
8. Test Permission Error: DELETE /api/comments/{id}/ (Delete a Comment by Non-Owner)
Request:

Method: DELETE
URL: http://localhost:8000/api/comments/1/
Headers:
Authorization: Token <non_owner_user_token>
Response:

Status Code: 403 Forbidden
Body:
json
Copy code
{
  "detail": "You cannot delete this comment."
}
Notes:

The error response is returned as the logged-in user does not own the comment.