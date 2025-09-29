from .models import Note
from django import forms

class NoteForm(forms.ModelForm):
    model = Note
    fields = ['title', 'content']