from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Note
from .forms import NoteForm

def index(request):
    notes = Note.objects.all().order_by('-created_at')
    context = {'title':'Мои заметки','notes':notes}
    return render(request, 'index.html', context)

@login_required
def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.save()
            return redirect('index')
    else:
        form = NoteForm()
    context = {'form': form, 'title':'Создание заметки'}
    return render (request, 'notes/create_note.html', context)

@login_required
def update_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if note.author != request.user:
        return redirect('index')
    
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.save()
            return redirect('index')
    else:
        form = NoteForm(instance=note)
    context = {'form':form, 'title':'Редактирование заметки'}
    return render(request, 'notes/update_note.html', context)