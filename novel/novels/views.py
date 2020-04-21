from django.shortcuts import render

def index(request):
    return render(request, '_layouts/homepage.html')
