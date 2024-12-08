from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Book, Author
from rest_framework.reverse import reverse

class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create a test user and login
        self.user = User.objects.create_user(username='testuser', password='password')
        self.admin_user = User.objects.create_superuser(username='admin', password='password')
        
        self.author = Author.objects.create(name='Test Author')

        self.book_data = {
            'title': 'Test Book',
            'author': self.author,
            'publication_year': '2023'
        }

        self.book = Book.objects.create(**self.book_data)
        self.url = reverse('book-list')

    def test_create_book(self):
        # Test that authenticated user can create a book
        self.client.login(username='testuser', password='password')
        response = self.client.post(self.url, self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_create_book_without_permission(self):
        # Test that non-authenticated user cannot create a book
        response = self.client.post(self.url, self.book_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_read_books(self):
        # Test retrieving all books
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_read_single_book(self):
        # Test retrieving a single book by its ID
        response = self.client.get(reverse('book-detail', args=[self.book.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Book')

    def test_update_book(self):
        # Test updating a book
        update_data = {'title': 'Updated Title'}
        response = self.client.put(reverse('book-detail', args=[self.book.id]), update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Title')

    def test_delete_book(self):
        # Test deleting a book
        response = self.client.delete(reverse('book-detail', args=[self.book.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_permission_admin(self):
        # Test that only admin can delete books
        self.client.login(username='admin', password='password')
        response = self.client.delete(reverse('book-detail', args=[self.book.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_filter_books(self):
        # Test filtering books by title
        Book.objects.create(title='Another Book', author=self.author, publication_year='2022')
        response = self.client.get(self.url + '?title=Test Book')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books(self):
        # Test ordering books by published date
        book_2 = Book.objects.create(title='Second Book', author=self.author, publication_year='2021')
        response = self.client.get(self.url + '?ordering=published_date')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Second Book')