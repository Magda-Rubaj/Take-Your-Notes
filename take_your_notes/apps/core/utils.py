from ..user.models import User
from ..category.models import Category
from ..note.models import Note


def create_user(**kwargs):
    if 'username' not in kwargs:
        kwargs['username'] = "user%d" % User.objects.all().count()

    if 'email' not in kwargs:
        kwargs['email'] = "%s@email.com" % kwargs['username']

    if 'password' not in kwargs:
        kwargs['password'] = "pass"

    return User.objects.create_user(**kwargs)

def create_category(**kwargs):
    if 'user' not in kwargs:
        kwargs['user'] = create_user()

    if 'name' not in kwargs:
        kwargs['name'] = "category%d" % Category.objects.all().count()

    return Category.objects.create(**kwargs)

def create_note(**kwargs):
    if 'name' not in kwargs:
        kwargs['name'] = "note%d" % Note.objects.all().count()

    if 'category' not in kwargs:
        kwargs['category'] = create_category()
    
    if 'content'not in kwargs:
        kwargs['content'] = "note_content%d" % Note.objects.all().count()
    
    return Note.objects.create(**kwargs)

