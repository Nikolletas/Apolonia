from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import UserRegistrationChangeForm, UserRegistrationForm
from .models import Profile

UserModel = get_user_model()


@admin.register(UserModel)
class MyUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', )
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
        ('Personal info', {'fields': ('first_name', 'last_name', 'apartment')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'user_permissions', 'groups', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', )}),
    )
