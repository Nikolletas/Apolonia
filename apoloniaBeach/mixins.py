from django.shortcuts import render


class UserIsApartmentOwnerMixin:
    def dispatch(self, request, *args, **kwargs):

        if not (request.user.apartment.exists() or request.user.is_superuser):
            return render(
                request,
                '403.html',
                {"message": "You are not permissions to do this."},
                status=403
            )
        return super().dispatch(request, *args, **kwargs)