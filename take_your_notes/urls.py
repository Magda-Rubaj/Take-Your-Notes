"""take_your_notes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic.base import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include(('take_your_notes.apps.user.urls', 'user'), namespace='user')),
    path('', include(('take_your_notes.apps.core.urls', 'core'), namespace='core')),
    path('categories/', include(('take_your_notes.apps.category.urls', 'categories'), namespace='categories')),
    path('notes/', include(('take_your_notes.apps.note.urls', 'notes'), namespace='notes')),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    #re_path(r'^.*$', RedirectView.as_view(url='/accounts/login', permanent=False), name='login')
]
