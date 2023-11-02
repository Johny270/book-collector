from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Book
from .forms import ReviewForm
from django.shortcuts import render, redirect


# Create your views here.

class BookCreate(CreateView):
  model = Book
  fields = '__all__'
  success_url = '/books/'

class BookUpdate(UpdateView):
  model = Book
  fields = ['author', 'description', 'year']

class BookDelete(DeleteView):
  model = Book
  success_url = '/books/'

def home(request):
  return HttpResponse('<h1>Hellow World</h1>')

def about(request):
  return render(request, 'about.html')

def book_index(request):
  books = Book.objects.all()
  return render(request, 'books/index.html', { 'books': books })

def book_detail(request, book_id):
  book = Book.objects.get(id=book_id)
  review_form = ReviewForm()
  return render(request, 'books/detail.html', { 
    'book': book,
    'review_form': review_form
  })

def add_review(request, book_id):
  form = ReviewForm(request.POST)

  if form.is_valid():
    new_review = form.save(commit=False)
    new_review.book_id = book_id
    new_review.save()
  return redirect('book-detail', book_id=book_id)