from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"{self.title} {self.author} {self.publication_year}"
# Create your models here.

def book(self):
    book = Book.objects.create(
        title = 'Bad roads in Ghana',
        author = 'Johnson Ackuaku',
        publication_year = 1972
    )

class Department(models.Model):
    name = models.CharField(max_length=100)
    clearance = models.TextField(default= 'High')

    def __str__(self):
        return self.name

    
def department(self):
    department = Department.objects.create(
    name = 'Finance',
    clearance = 'High'
    )

 

class Employee(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')
    
    def __str__ (self):
        return self.name

def employee(self):
    employee = Employee.objects.create(
        name = 'Michael',
        department = 'Finance'
    )

    
class Product(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Detail(models.Model):
    description = models.TextField()
    product = models.OneToOneField(Product, related_name='details', on_delete=models.CASCADE)


class Students (models.Model):
    name = models.CharField(max_length=150)

class Courses (models.Model):
    name = models.CharField(max_length=150)
    students=models.ManyToManyField(Students, related_name='courses')