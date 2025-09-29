from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path('create_note/', views.create_note, name='create_note'),
    path('update_note/<int:note_id>/', views.update_note, name='update_note'),
    path('delete_note/<int:note_id>/', views.delete_note, name='delete_note'),
]