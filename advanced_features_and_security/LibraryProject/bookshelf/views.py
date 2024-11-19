from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, UserProfile, Library
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import user_passes_test
from .forms import ExampleForm, CustomUserCreationForm, BookForm   
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import permission_required

def index(request):
    return render (request, 'index.html')

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request,user)
            return redirect('login')
        
    else:
        form = CustomUserCreationForm()

    context = {'form': form}
    return render (request, 'bookshelf/register.html', context)

class LoginView(LoginView):
    template_name = 'bookshelf/login.html'


class LogoutView(LogoutView):
    next_page = 'login'


def list_books(request):
    books = Book.objects.all()
    return render (request, 'bookshelf/list_books.html', {'books':books})

class LibraryListView(ListView):
    model = Library
    template_name = 'bookshelf/library_detail.html'

def index_view(request):
    return render (request, 'bookshelf/index.html')

def user_is_admin(user):
    return user.profile.role == 'Admin'

@user_passes_test(user_is_admin)
def myadmin_view(request):
    return render(request, 'bookshelf/myadmin_view.html')

def user_is_librarian(user):
    return user.profile.role == 'Librarian'

@user_passes_test(user_is_librarian)
def librarian_view(request):
    return render(request, 'bookshelf/librarian_view.html')


def user_is_member(user):
    return user.profile.role == 'Member'


@user_passes_test(user_is_member)
def member_view(request):
    return render(request, 'bookshelf/member_view.html')

#Create a new book (Add)
@permission_required('bookshelf.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
        
    else:
        form = BookForm()
    return render(request, 'bookshelf/add_book.html', {'form':form})

#Edit an existing book(Edit)
@permission_required('bookshelf.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    
    else:
        form = BookForm(instance=book)
    return render(request, 'bookshelf/edit_book.html', {'form':form, 'book':book})

#Delete a book
@permission_required('bookshelf.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'bookshelf/delete_book.html', {'book':book})


def ExampleFormView(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            search_term = form.cleaned_data['search_term']
            books = Book.objects.filter(title__icontains=search_term)
            return render(request, 'bookshelf/form_example.html', {'books': books})
    else:
        form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})