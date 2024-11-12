from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import Profile
from .forms import UserRegistrationForm, ProfileCreateForm

UserModel = get_user_model()


class UserRegistrationView(CreateView):
    model = UserModel
    form_class = UserRegistrationForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('accounts/create-profile')


class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreateForm
    template_name = 'accounts/create-profile.html'
    success_url = reverse_lazy('base.html')