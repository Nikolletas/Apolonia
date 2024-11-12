from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Profile

UserModel = get_user_model()


class UserRegistrationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ('email', )


class UserRegistrationChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserModel


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        error_messages = {
            'required': 'This field is required!',
        }