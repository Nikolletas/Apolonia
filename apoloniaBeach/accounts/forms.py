from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Profile

UserModel = get_user_model()


class UserRegistrationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ('email', 'first_name', 'last_name', 'nationality', 'phone_number',)

        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'email@email.com'}),
            'first_name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Surname'}),
            'nationality': forms.TextInput(attrs={'placeholder': 'Nationality'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Phone Number'}),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''

        self.fields['password1'].widget.attrs.update({'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'The same password as before'})


class UserRegistrationChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UserModel


class UserEditForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['first_name', 'last_name', 'nationality', 'phone_number']


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_picture']

