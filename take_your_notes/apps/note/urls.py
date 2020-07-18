from django.urls import path
from .views import NoteCreationView


urlpatterns = [
    path(r'<int:pk>/create/',NoteCreationView.as_view(), name='create'),
]
