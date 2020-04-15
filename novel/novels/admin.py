from django.contrib import admin
from .models import Novel,Chapter, Genre

admin.site.site_header = "Light Novel Dashboard"

admin.site.register(Novel)
admin.site.register(Chapter)
admin.site.register(Genre)