from django.urls import path

from apoloniaBeach.accounts import views

urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name='register-user'),
    path('create_profile/', views.ProfileCreateView.as_view(), name='create-profile'),
]