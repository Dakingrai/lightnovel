from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:slug>/id=<int:id>', views.readnovel, name="novel"),
    path('<slug:slug>/chapter=<int:chapter>', views.readchapter, name="chapter")
]