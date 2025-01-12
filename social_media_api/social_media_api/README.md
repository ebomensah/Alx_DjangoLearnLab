# Social Media API

A Django-based API for handling user authentication and profile management. This project includes functionality for user registration, login, and retrieving user profiles with token-based authentication using Django REST Framework and Django's custom user model.

## Features

- User registration with custom fields (`bio`, `profile_picture`, `followers`).
- Token-based authentication for login and session management.
- Secure user profile management with endpoints to retrieve user data.
- Custom user model extending Django’s `AbstractUser`.

## Requirements

- Python 3.x
- Django 4.x
- Django REST Framework
- Pillow (for image handling)

## Setup Instructions

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/ebomensah/social-media-api.git
cd social-media-api

2. Install Dependencies

3. Configure the database

4. Create a superuser(optional)

5. Run the development server 


How to register users:
Endpoint: POST /api/accounts/register/

Request body:
{
    "username": "user1",
    "email": "user1@example.com",
    "password": "password123",
    "bio": "Hello, I am user1!",
    "profile_picture": "image_file_url_or_base64_encoded_image"
}

Response: {
    "token": "your_token_here"
}


User Login:
Endpoint: POST /api/accounts/login/
request body:
{
    "username": "user1",
    "password": "password123"
}

Response:
{
    "token": "your_token_here"
}

Custom User Model
The CustomUser model extends Django’s AbstractUser and includes additional fields:

bio: A text field for the user’s biography (optional).
profile_picture: An image field to store the user's profile picture (optional).
followers: A Many-to-Many relationship with the CustomUser model to represent users that follow each other.