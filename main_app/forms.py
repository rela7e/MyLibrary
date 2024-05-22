from django.forms import ModelForm
from .models import Note
from django.contrib.auth.forms import UserCreationForm

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['content']
        labels = { 'content': ''}

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove specific help text for the password field
        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

