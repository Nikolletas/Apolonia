from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import UserRegistrationChangeForm, UserRegistrationForm

UserModel = get_user_model()


@admin.register(UserModel)
class MyUserAdmin(UserAdmin):
    list_display = ('email', )
    form = UserRegistrationChangeForm
    add_form = UserRegistrationForm
    ordering = ('pk',)

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        })
    )

    fieldsets = (
        ('Credentials', {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'groups', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
