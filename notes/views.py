from django.shortcuts import render
from .models import Note

def index(request):
    note = Note.objects.all()
    context = {'title':'Мои заметки','note':note}
    return render(request, 'index.html', context)