from django.contrib import admin
from .models import Novel,Chapter, Genre
from import_export.admin import ImportExportModelAdmin

class ChapterInline(admin.TabularInline):
    model = Chapter

@admin.register(Novel)
class NovelAdmin(admin.ModelAdmin):
    fields = (
        ('name', 'featured'),
        'status',
        'author',
        'picture',
        'description',
        'genre',
    )

    save_on_top = True
    list_display = ['id','name', 'created_at', 'updated_at', 'status', 'author']
    list_filter = ['status', 'updated_at']
    date_hierarchy = 'updated_at'
    search_fields = ['name', 'description']
    ordering = ['created_at']
    list_editable = ['status']
    filter_horizontal = ['genre']

    inlines = [ChapterInline]


@admin.register(Chapter)
class ChapterAdmin(ImportExportModelAdmin):
    from_encoding = 'utf-8'
    raw_id_fields = ("novel",)
    fields = (
        ('chapter', 'name'),
        'novel',
        'chapter_content',
    )
    list_display = ['id','novel','name','chapter']

    search_fields = ['novel']


@admin.register(Genre)
class GenreAdmin(ImportExportModelAdmin):
    list_display = ['id', 'name', 'created_at']


