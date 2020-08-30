from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.views.generic.edit import CreateView, FormView, DeleteView
from django.views.generic import DetailView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .forms import NoteForm
from .models import Note
from ..category.models import Category


class NoteCreationView(CreateView):
    form_class = NoteForm
    template_name = 'note/note_create.html'
    success_url = reverse_lazy('categories:all')

    @method_decorator(login_required())
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.category = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super(NoteCreationView, self).form_valid(form)
    
class NoteDetailView(DetailView):
    model = Note

    @method_decorator(login_required())
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class NoteUpdateView(UpdateView):
    form_class = NoteForm
    success_url = reverse_lazy('categories:all')
    model = Note
    template_name = 'note/note_update.html'

    @method_decorator(login_required())
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class NoteDeleteView(DeleteView):
    model = Note
    success_url = reverse_lazy('categories:all')

    @method_decorator(login_required())
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
