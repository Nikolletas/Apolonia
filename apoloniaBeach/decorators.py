
from functools import wraps

from django.contrib.auth.models import Group
from django.http import HttpResponseForbidden


def user_is_apartment_owner(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden("You need to log in to access this page.")

        if not (request.user.apartment.all().exists() or request.user.is_superuser):
            print(request.user.apartment.all())
            return HttpResponseForbidden("You are not an apartment owner.")

        return view_func(request, *args, **kwargs)
    return _wrapped_view


def user_is_manager(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        manager_group = Group.objects.get(name="Manager")
        if not request.user.is_authenticated:
            return HttpResponseForbidden("You need to log in to access this page.")

        if not (manager_group in request.user.groups.all() or request.user.is_superuser):
            return HttpResponseForbidden("You are not permissions to do this.")

        return view_func(request, *args, **kwargs)
    return _wrapped_view
