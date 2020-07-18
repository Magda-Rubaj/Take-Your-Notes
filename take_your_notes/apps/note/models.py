from django.db import models
from ckeditor.fields import RichTextField
from ..category.models import Category

class Note(models.Model):
    name = models.CharField(max_length=30)
    content = RichTextField(default=None)
    date_added = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)

