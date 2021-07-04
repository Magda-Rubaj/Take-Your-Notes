from take_your_notes.apps.category.models import Category


def category_context(request):
    return {
        'category_list': Category.objects.all()
    }