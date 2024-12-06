from django.shortcuts import render, redirect, get_object_or_404
from .models import Library, Book, UserProfile
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import user_passes_test
from .forms import BookForm 
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import permission_required

def index(request):
    return render (request, 'index.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate (username=username, password=password)
            login(request,user)
            return redirect('login')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render (request, 'relationship_app/register.html', context)

class LoginView(LoginView):
    template_name = 'relationship_app/login.html'


class LogoutView(LogoutView):
    next_page = 'login'


def list_books(request):
    books = Book.objects.all()
    return render (request, 'relationship_app/list_books.html', {'books':books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'

def index_view(request):
    return render (request, 'relationship_app/index.html')

def user_is_admin(user):
    return user.profile.role == 'Admin'

@user_passes_test(user_is_admin)
def admin_view(request):
    return render(request, 'relationship_app/myadmin_view.html')

def user_is_librarian(user):
    return user.profile.role == 'Librarian'

@user_passes_test(user_is_librarian)
def Librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')


def user_is_member(user):
    return user.profile.role == 'Member'


@user_passes_test(user_is_member)
def Member_view(request):
    return render(request, 'relationship_app/member_view.html')

#Create a new book (Add)
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')
        
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form':form})

#Edit an existing book(Edit)
@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/edit_book.html', {'form':form, 'book':book})

#Delete a book
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'relationship_app/delete_book.html', {'book':book})
