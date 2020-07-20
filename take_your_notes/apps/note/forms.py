from django import forms
from django.forms import ValidationError
from django.db.models import Q
from django.utils.translation import gettext as _
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('name', 'content',)
        widgets = {
            'content': CKEditorUploadingWidget(),
        }


