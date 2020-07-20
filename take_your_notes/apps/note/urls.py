from django.urls import path
from .views import NoteCreationView, NoteDetailView, NoteUpdateView


urlpatterns = [
    path(r'<int:pk>/create/',NoteCreationView.as_view(), name='create'),
    path(r'detail/<int:pk>/', NoteDetailView.as_view(), name='note-detail'),
    path(r'edit/<int:pk>/', NoteUpdateView.as_view(), name='note-edit'),
]
