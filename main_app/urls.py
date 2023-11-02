from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('books/', views.book_index, name='book-index'),
    path('books/<int:book_id>', views.book_detail, name='book-detail'),
    path('books/create/', views.BookCreate.as_view(), name='book-create'),
    path('books/<int:pk>/update', views.BookUpdate.as_view(), name='book-update'),
    path('books/<int:pk>/delete', views.BookDelete.as_view(), name='book-delete'),
    path('books/<int:book_id>/add-review/', views.add_review, name='add-review'),
    path('books/<int:book_id>/assoc-cover/<int:cover_id>/', views.assoc_cover, name='assoc-cover'),
    path('accounts/signup/', views.signup, name='signup'),
    path('covers/create/', views.CoverCreate.as_view(), name='cover-create'),
    path('covers/<int:pk>/', views.CoverDetail.as_view(), name ='cover-detail'),
    path('covers/', views.CoverList.as_view(), name='cover-index'),
    path('covers/<int:pk>/update/', views.CoverUpdate.as_view(), name='cover-update'),
    path('covers/<int:pk>/delete/', views.CoverDelete.as_view(), name='cover-delete'),
]
