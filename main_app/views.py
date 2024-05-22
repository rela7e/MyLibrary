from django.shortcuts import render, redirect

from django.views.generic import CreateView, UpdateView, DeleteView

from .models import Book, Note, AssociateBookUser

from .forms import NoteForm

from .filters import BookFilter

from django.contrib.auth import login

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import get_object_or_404

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def books_index(request):
    books = Book.objects.all()
    if request.GET:
        book_filter = BookFilter(request.GET, queryset=books)
        books = book_filter.qs
    else:
        book_filter = BookFilter(queryset=books)
    return render(request, 'books/index.html', {'filter': book_filter, 'books': books})

def books_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    user = request.user
    notes = book.note_set.filter(user=user)
    note_form = NoteForm()
    return render(request, 'books/detail.html', { 'book': book, 'note_form': note_form, 'notes': notes })

class BookCreate(CreateView):
    model = Book
    fields = '__all__'
    
class BookUpdate(UpdateView):
    model = Book
    fields = '__all__'

class BookDelete(DeleteView):
    model= Book
    success_url = '/books'

def add_note(request, book_id):
    form = NoteForm(request.POST)
    if form.is_valid():
        new_note = form.save(commit=False)
        new_note.book_id = book_id
        new_note.save()
    return redirect('detail', book_id=book_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else: error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)    

def my_books(request):
    user_books = AssociateBookUser.objects.filter(user=request.user)
    return render(request, 'my_books.html', {'user_books': user_books})

def add_to_my_books(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        book = get_object_or_404(Book, id=book_id)
        AssociateBookUser.objects.create(user=request.user, book=book)
        return redirect('books_index')
    else:
        pass

def unassoc_book(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        association = get_object_or_404(AssociateBookUser, user=request.user, book_id=book_id)
        association.delete()
        return redirect('my_books') 
    else:
        pass
