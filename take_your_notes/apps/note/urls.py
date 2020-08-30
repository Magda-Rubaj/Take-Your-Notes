from django.urls import path
from .views import NoteCreationView, NoteDetailView, NoteUpdateView, NoteDeleteView


urlpatterns = [
    path(r'<int:pk>/create/',NoteCreationView.as_view(), name='create'),
    path(r'detail/<int:pk>/', NoteDetailView.as_view(), name='detail'),
    path(r'edit/<int:pk>/', NoteUpdateView.as_view(), name='edit'),
    path(r'delete/<int:pk>/', NoteDeleteView.as_view(), name='delete'),
]
