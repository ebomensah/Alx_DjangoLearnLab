from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Book, Employee
from django.http import HttpResponse
# Create your views here.

def book_list(request):
    queryset = Book.objects.all()
    context = {'book_list': queryset}
    return render(request, 'bookshelf/book_list.html',context)

class hello_view(TemplateView):
    template_name = 'bookshelf/hello.html'

def about(request):
    return render(request, 'bookshelf/about.html', {'name': 'Ebo Mensah'})

def homepage(request):
    return HttpResponse('homepage')

class EmployeeListView(ListView):
    model = Employee
    template_name = 'bookshelf/employee_list.html'
    