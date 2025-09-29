from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Note
from .forms import NoteForm

def index(request):
    note = Note.objects.filter()
    context = {'title':'Мои заметки','note':note}
    return render(request, 'index.html', context)

@login_required
def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect()


@login_required
def update_note(request):
    pass