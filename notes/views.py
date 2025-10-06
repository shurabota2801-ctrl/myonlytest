from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Note
from .forms import NoteForm
from django.urls import reverse

def index(request):
    return render(request, 'index.html', {'title':'Мои тесты'})

@login_required
def notes_list(request):
    notes = Note.objects.filter(author=request.user).order_by('-created_at')
    search_query = request.GET.get('q', '')
    if search_query:
        notes = notes.filter(author=request.user).filter(Q(title__icontains=search_query) | Q(content__icontains=search_query)).order_by('-created_at')

    paginator = Paginator(notes, 4)
    page_number = request.GET.get('page')
    page_notes = paginator.get_page(page_number)

    context = {
        'title':'Мои заметки',
        'notes':notes,
        'search_query':search_query,
        'page_notes': page_notes,
    }
    return render(request, 'notes/notes_list.html', context)

@login_required
def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.save()
            return redirect(reverse('notes:notes_list'))
    else:
        form = NoteForm()
    context = {'form': form, 'title':'Создание заметки'}
    return render (request, 'notes/create_note.html', context)

@login_required
def update_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.save()
            return redirect(reverse('notes:notes_list'))
    else:
        form = NoteForm(instance=note)
    context = {'form':form, 'title':'Редактирование заметки'}
    return render(request, 'notes/update_note.html', context)

@login_required
def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, author=request.user)
    if request.method == 'POST':
        note.delete()
        return redirect('notes:notes_list')
    context = {'note':note, 'title':'Удаление заметки'}
    return render(request, 'notes/delete_note.html', context)