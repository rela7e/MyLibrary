from django.contrib.auth.models import User
from django.db import models

from django.urls import reverse

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    published = models.IntegerField
    ISBN = models.TextField(unique=True)

    def __str__(self):
        return f'{self.title} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'book_id': self.id})
    
class Note(models.Model):
    content = models.CharField(max_length=250)

    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.content} ({self.id})'

class AssociateBookUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} - {self.book.title}'