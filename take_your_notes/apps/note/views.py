from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.views.generic.edit import CreateView, FormView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from .forms import NoteCreationForm
from .models import Note
from ..category.models import Category


class NoteCreationView(CreateView):
    form_class = NoteCreationForm
    template_name = 'note/note.html'
    success_url = reverse_lazy('categories:all')

    @method_decorator(login_required())
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        form.instance.category = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super(NoteCreationView, self).form_valid(form)
    
