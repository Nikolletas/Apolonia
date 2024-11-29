from django.urls import path, include

from apoloniaBeach.common import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('rules/', views.rules, name='rules'),
    path('contacts/', views.contacts, name='contacts'),
    path('documents/', views.documents, name='documents'),
    path('home_book/', views.home_book, name='home-book'),
    path('all_documents/', views.association_documents, name='all-documents'),
    path('document_add/', views.association_document_add, name='document-add'),
    path('announcements/', views.announcements, name='announcements'),
    path('announcement_add/', views.announcement_add, name='announcement-add'),
    path('<int:pk>/', include([
        path('document_edit/', views.association_document_edit, name='document-edit'),
        path('document_delete/', views.association_document_delete, name='document-delete'),
        path('announcement_edit/', views.announcement_edit, name='announcement-edit'),
        path('announcement_delete/', views.announcement_delete, name='announcement-delete')
    ])),
]