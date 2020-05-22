from django.urls import path
from .views import CategoryCreateView, CategoryListView


urlpatterns = [
    path('create/',CategoryCreateView.as_view(), name='create'),
    path('all/',CategoryListView.as_view(), name='all'),
]

