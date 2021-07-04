from django.urls import path
from .views import CategoryCreateView, CategoryDetailView, CategoryDeleteView


urlpatterns = [
    path('create/',CategoryCreateView.as_view(), name='create'),
    path(r'detail/<int:pk>/', CategoryDetailView.as_view(), name='detail'),
    path(r'delete/<int:pk>/', CategoryDeleteView.as_view(), name='delete'),
]

