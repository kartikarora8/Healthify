from django.contrib import admin
from .models import blogs, Tag

admin.site.register(blogs)
admin.site.register(Tag)