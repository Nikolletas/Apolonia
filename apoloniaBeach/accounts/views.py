from django.contrib import messages
from django.contrib.auth import get_user_model, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseForbidden, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from .models import Profile
from .forms import UserRegistrationForm, ProfileEditForm, UserEditForm

UserModel = get_user_model()


class MyUserCreationView(CreateView):
    model = UserModel
    form_class = UserRegistrationForm
    template_name = 'accounts/register-page.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


class UserLoginView(LoginView):
    template_name = 'accounts/login.html'


class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    template_name = 'accounts/profile-edit-page.html'
    form_class = ProfileEditForm

    def test_func(self):
        return self.request.user == self.get_object().user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_form'] = UserEditForm(instance=self.request.user)
        print(context)
        return context

    def form_valid(self, form):
        user_form = UserEditForm(self.request.POST, instance=self.request.user)
        if user_form.is_valid():
            user_form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('profile-details', kwargs={'pk': self.object.pk})


class ProfileDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Profile
    template_name = 'accounts/profile-confirm-delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        profile = get_object_or_404(Profile, pk=self.kwargs['pk'])
        return self.request.user == profile.user


@login_required
def profile_details(request, pk):

    user = request.user
    profile = Profile.objects.get(pk=pk)

    if profile.user != user:
        return HttpResponseForbidden("You do not have permission to view this profile.")

    context = {
        'user': user,
        'profile': profile,
    }
    return render(request, 'accounts/profile-details.html', context)


@login_required
def change_password(request):
    form = PasswordChangeForm(request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile-details', pk=request.user.pk)
        else:
            messages.error(request, 'Please correct the error below.')

    context = {
        'form': form
    }
    return render(request, 'accounts/change-password.html', context)

