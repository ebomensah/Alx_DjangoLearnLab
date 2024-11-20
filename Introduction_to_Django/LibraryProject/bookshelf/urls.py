from django.urls import path
from .views import hello_view, EmployeeListView
from . import views 

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('employees/', EmployeeListView.as_view(), name='employee_list'),
    path ('hello/', hello_view.as_view(), name='hello'),
    path('about/', views.about, name = 'about'),
    path('', views.homepage)
]
