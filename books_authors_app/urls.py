from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('addauthors', views.index2),
    path('addauthor/<int:bookId>', views.addauthor),
    path('addbook/<int:authorId>', views.addbook),
    path('processbook', views.processbook),
    path('processauthor', views.processauthor),
    path('viewbook/<int:bookId>', views.viewBook),
    path('viewauthor/<int:authorId>', views.viewAuthor)
]