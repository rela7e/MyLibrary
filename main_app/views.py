from django.shortcuts import render, redirect

from django.views.generic import CreateView, UpdateView, DeleteView

from .models import Book

from .forms import NoteForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def books_index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {
        'books': books
    })

def books_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    note_form = NoteForm()
    return render(request, 'books/detail.html', { 'book': book, 'note_form': note_form })

class BookCreate(CreateView):
    model = Book
    fields = '__all__'
    
class BookUpdate(UpdateView):
    model = Book
    fields = ['description']

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