from django.http import HttpResponseForbidden


class UserIsApartmentOwnerMixin:
    def dispatch(self, request, *args, **kwargs):

        if not (request.user.apartment.exists() or request.user.is_superuser):
            return HttpResponseForbidden("You are not an apartment owner.")
        return super().dispatch(request, *args, **kwargs)