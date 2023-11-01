from django.shortcuts import render
from django.http import HttpResponse

class Book:
  def __init__(self, title, author, description, year):
    self.title = title
    self.author = author
    self.description = description
    self.year = year

books = [
  Book('Think and Grow Rich', 'Napoleon Hill', 'A book about success', '1900'),
  Book('Think and Grow Rich', 'Napoleon Hill', 'A book about success', '1900'),
  Book('Think and Grow Rich', 'Napoleon Hill', 'A book about success', '1900')
]

# Create your views here.
def home(request):
  return HttpResponse('<h1>Hellow World</h1>')

def about(request):
  return render(request, 'about.html')

def book_index(request):
  return render(request, 'books/index.html', { 'books': books })
