from django import template
from ...note.models import Note


register = template.Library()

@register.filter(name='note_list')
def note_list(value):
    query = Note.objects.filter(category=value)
    return query
