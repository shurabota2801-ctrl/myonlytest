from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path('create/', views.create_note, name='note_create'),
    path('<int:note_id>/update/', views.update_note, name='note_update'),
    path('<int:note_id>/delete/', views.delete_note, name='note_delete'),
    path('', views.notes_list, name='notes_list'),
]