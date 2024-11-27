from django.urls import path

from apoloniaBeach.common import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('rules/', views.rules, name='rules'),
    path('contacts/', views.contacts, name='contacts'),
    path('documents/', views.documents, name='documents'),
    path('home_book/', views.home_book, name='home-book'),
]