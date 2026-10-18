# w pliku hoby_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),       
    path('about/', views.about_view, name='hobby'),
    path('gallery/', views.gallery_view, name='moje_przyklady'),
]