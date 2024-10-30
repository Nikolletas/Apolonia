from django.urls import path

from apoloniaBeach.houses import views

urlpatterns = [
    path('', views.index, name='index'),
]