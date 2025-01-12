GET /api/posts/
  Description: Retrieves a list of all posts, with pagination.
  Response:
    - Status: 200 OK
    - Body: 
      [
        {
          "id": 1,
          "author": 1,
          "title": "First Post",
          "content": "This is the first post.",
          "created_at": "2025-01-12T12:34:56Z",
          "updated_at": "2025-01-12T12:34:56Z"
        },
        ...
      ]
    
POST /api/posts/
  Description: Creates a new post. The user is automatically set as the author.
  Request Body:
    {
      "title": "New Post",
      "content": "This is a new post."
    }
  Response:
    - Status: 201 Created
    - Body:
      {
        "id": 2,
        "author": 2,
        "title": "New Post",
        "content": "This is a new post.",
        "created_at": "2025-01-12T12:45:00Z",
        "updated_at": "2025-01-12T12:45:00Z"
      }

GET /api/comments/?post=1
  Description: Retrieves comments related to a specific post.
  Response:
    - Status: 200 OK
    - Body:
      [
        {
          "id": 1,
          "author": 1,
          "post": 1,
          "content": "Great post!",
          "created_at": "2025-01-12T12:35:00Z",
          "updated_at": "2025-01-12T12:35:00Z"
        },
        ...
      ]

Follow a User
Endpoint: POST /accounts/follow/<user_id>/
Description: Follows the user with the given user_id.
Request Body: None
Response:
200 OK: Successfully followed the user.
400 Bad Request: You cannot follow yourself.
Unfollow a User
Endpoint: POST /accounts/unfollow/<user_id>/
Description: Unfollows the user with the given user_id.
Request Body: None
Response:
200 OK: Successfully unfollowed the user.
400 Bad Request: You cannot unfollow yourself.
View Feed
Endpoint: GET /posts/feed/
Description: Retrieves a feed of posts from users the current user follows, ordered by creation date.
Response: List of posts with fields such as id, user, content, and created_at.