from django.contrib.auth.views import LogoutView
from django.urls import path, include

from apoloniaBeach.accounts import views


urlpatterns = [
    path('register/', views.MyUserCreationView.as_view(), name='register-user'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('<int:pk>/', include([
        path('details/', views.profile_details, name='profile-details'),
        path('profile-edit/', views.ProfileEditView.as_view(), name='profile-edit'),
        path('profile-delete/', views.ProfileDeleteView.as_view(), name='profile-delete'),
        ])),
]