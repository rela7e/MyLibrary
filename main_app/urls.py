from django.urls import path
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='home/', permanent=True)),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('books/', views.books_index, name='books_index'),
    path('books/<int:book_id>/', views.books_detail, name='detail'),
    path('books/create/', views.BookCreate.as_view(), name='books_create'),
    path('books/<int:pk>/update/', views.BookUpdate.as_view(), name='books_update'),
    path('books/<int:pk>/delete/', views.BookDelete.as_view(), name='books_delete'),
    path('books/<int:book_id>/add_note/', views.add_note, name='add_note'),
    path('accounts/signup/', views.signup, name='signup'),
    path('books/my_books/', views.my_books, name='my_books' ),
    path('add_to_my_books/', views.add_to_my_books, name='add_to_my_books'),
    path('unassoc_book/', views.unassoc_book, name='unassoc_book'),
]