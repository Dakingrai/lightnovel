from django.shortcuts import render
from .models import Novel, Chapter

def index(request):

    featured_novels = Novel.objects.filter(featured=2)
    context = {
        'featured_novels': featured_novels,
    }
    return render(request, '_layouts/homepage.html', context)

def readnovel(request, slug, id):
    novel = Novel.objects.get(id=id)
    descending_chapters = Chapter.objects.filter(novel=id).order_by('-id')[:5]

    args = {
        'novel': novel,
        'descending_chapters': descending_chapters,
    }

    return render(request, 'novels/novel.html', args)

def readchapter(request, slug, id, chapter):
    chapter = Chapter.objects.get(id=id)
    try:
        next_chapter = Chapter.objects.get(chapter=chapter.chapter+1.0)
    except:
        next_chapter = '#'
    try:
        prev_chapter = Chapter.objects.get(chapter=chapter.chapter-1.0)
    except:
        prev_chapter = '#'
    args = {
        'chapter': chapter,
        'next_chapter': next_chapter,
        'prev_chapter': prev_chapter,
    }
    return render(request, 'novels/chapter.html', args)

