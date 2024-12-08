from django.urls import path, include

from apoloniaBeach.houses import views

urlpatterns = [
    path('houses', views.houses, name='houses'),
    path('add_house/', views.add_house, name='add-house'),
    path('apartments/', views.apartments, name='apartments'),
    path('add_apartment/', views.add_apartment, name='add-apartment'),
    path('<int:pk>/', include([
        path('edit_house', views.edit_house, name='edit-house'),
        path('details_apartment/', views.details_apartment, name='details-apartment'),
        path('edit_apartment/', views.edit_apartment, name='edit-apartment'),
        path('delete_apartment/', views.delete_apartment, name='delete-apartment'),
    ]))
]