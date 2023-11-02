from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Book, Cover
from .forms import ReviewForm
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class BookCreate(LoginRequiredMixin, CreateView):
  model = Book
  fields = ['title', 'author', 'description', 'year']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

  success_url = '/books/'

class BookUpdate(LoginRequiredMixin, UpdateView):
  model = Book
  fields = ['author', 'description', 'year']

class BookDelete(LoginRequiredMixin, DeleteView):
  model = Book
  success_url = '/books/'

class CoverCreate(LoginRequiredMixin, CreateView):
  model = Cover
  fields = '__all__'

class CoverList(LoginRequiredMixin, ListView):
  model = Cover

class CoverDetail(LoginRequiredMixin, DetailView):
  model = Cover

class CoverUpdate(LoginRequiredMixin, UpdateView):
  model = Cover
  fields = ['cover_type', 'color']

class CoverDelete(LoginRequiredMixin, DeleteView):
  model = Cover
  success_url = '/covers/'

class Home(LoginView):
  template_name = 'home.html'

def home(request):
  return HttpResponse('<h1>Hellow World</h1>')

def about(request):
  return render(request, 'about.html')

@login_required
def book_index(request):
  books = Book.objects.filter(user=request.user)
  return render(request, 'books/index.html', { 'books': books })

@login_required
def book_detail(request, book_id):
  book = Book.objects.get(id=book_id)
  covers_book_dont_have = Cover.objects.exclude(id__in = book.covers.all().values_list('id'))
  review_form = ReviewForm()
  return render(request, 'books/detail.html', { 
    'book': book,
    'review_form': review_form,
    'covers': covers_book_dont_have
  })

@login_required
def add_review(request, book_id):
  form = ReviewForm(request.POST)

  if form.is_valid():
    new_review = form.save(commit=False)
    new_review.book_id = book_id
    new_review.save()
  return redirect('book-detail', book_id=book_id)

@login_required
def assoc_cover(request, book_id, cover_id):
  Book.objects.get(id=book_id).covers.add(cover_id)
  return redirect('book-detail', book_id=book_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('book-index')
    else:
      error_message = 'Invalid sign up - try again'

  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)
