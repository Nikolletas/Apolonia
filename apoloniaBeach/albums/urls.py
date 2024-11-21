from django.urls import path, include

from apoloniaBeach.albums import views

urlpatterns = [
    path('photo_add/', views.PhotoAddPageView.as_view(), name='add-photo'),
    path('photo_common_add/', views.AddCommonPhotoView.as_view(), name='photo-common-add'),
    path('photo_rental_add/', views.AddRentalPhotoView.as_view(), name='photo-rental-add'),
    path('photo_sale_add/', views.AddSalePhotoView.as_view(), name='photo-sale-add'),
    path('common_photos/', views.CommonPhotosView.as_view(), name='common-photos'),
    path('rental_photos/', views.RentalPhotosView.as_view(), name='rental-photos'),
    path('sale_photos/', views.SalePhotosView.as_view(), name='sale-photos'),
    path('<int:pk>/', include([
        path('detail_photos/', views.DetailPhotosView.as_view(), name='detail-photos'),
        path('edit_photo/', views.EditPhotoView.as_view(), name='edit-photo'),
        path('delete_photo/', views.DeletePhotoView.as_view(), name='delete-photo'),
    ]))
]