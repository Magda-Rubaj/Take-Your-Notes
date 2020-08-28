from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render
from django.views.generic.edit import DeleteView
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy
from .models import Category


class CategoryListView(ListView):
    model = Category
    template_name = 'category/category_list.html'

    @method_decorator(login_required())
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class CategoryCreateView(CreateView):
    model = Category
    fields=('name',)
    template_name = 'category/category_create.html'
    success_url = reverse_lazy('categories:all')

    
    def get_form_kwargs(self):
        kwargs = super(CategoryCreateView, self).get_form_kwargs()
        if kwargs['instance'] is None:
            kwargs['instance'] = Category()
        kwargs['instance'].user = self.request.user
        return kwargs

    @method_decorator(login_required())
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class CategoryDetailView(DetailView):
    model = Category

    @method_decorator(login_required())
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('categories:all')

    @method_decorator(login_required())
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
