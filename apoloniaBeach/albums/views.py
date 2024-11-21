from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView, DetailView, UpdateView, DeleteView

from .forms import AddCommonPhotoForm, AddRentalPhotoForm, AddSalePhotoForm, EditRentalPhotoForm, EditSalePhotoForm, \
    EditCommonPhotoForm
from .models import Album
from ..choices import PhotoTypesChoices


class PhotoAddPageView(TemplateView):
    template_name = 'gallery/add-photo.html'


class AddCommonPhotoView(CreateView):
    model = Album
    form_class = AddCommonPhotoForm
    template_name = 'gallery/photo-add.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.photo_type = PhotoTypesChoices.COMMON
        form.instance.published_by = get_user_model().objects.get(pk=self.request.user.pk)
        return super().form_valid(form)


class AddRentalPhotoView(CreateView):
    model = Album
    form_class = AddRentalPhotoForm
    template_name = 'gallery/photo-add.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.photo_type = PhotoTypesChoices.RENTAL
        form.instance.published_by = get_user_model().objects.get(pk=self.request.user.pk)

        form.instance.apartment.for_rental = True
        form.instance.apartment.save()

        return super().form_valid(form)

    print(get_user_model().objects.all())


class AddSalePhotoView(CreateView):
    model = Album
    form_class = AddSalePhotoForm
    template_name = 'gallery/photo-add.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.photo_type = PhotoTypesChoices.SALE
        form.instance.published_by = get_user_model().objects.get(pk=self.request.user.pk)

        form.instance.apartment.for_sale = True
        form.instance.apartment.save()

        return super().form_valid(form)


class CommonPhotosView(ListView):
    model = Album
    template_name = 'gallery/common-photos.html'
    context_object_name = 'photos'
    paginate_by = 2

    def get_queryset(self):
        return super().get_queryset().filter(photo_type='Common').order_by('published_by')


class RentalPhotosView(ListView):
    model = Album
    template_name = 'gallery/rental-photos.html'
    context_object_name = 'photos'
    paginate_by = 2

    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .filter(photo_type='Rental')
            .order_by('apartment', 'published_by')
        )


class SalePhotosView(ListView):
    model = Album
    template_name = 'gallery/sale-photos.html'
    context_object_name = 'photos'
    paginate_by = 2

    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .filter(photo_type='Sale')
            .order_by('apartment', 'published_by')
        )


class DetailPhotosView(ListView):
    model = Album
    template_name = 'gallery/detail-photos.html'
    context_object_name = 'photos_for_apartment'
    paginate_by = 2

    def get_queryset(self):
        photo = Album.objects.get(pk=self.kwargs['pk'])
        self.apartment = photo.apartment
        return Album.objects.filter(apartment=self.apartment)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['apartment'] = self.apartment
        return context


class EditPhotoView(UpdateView):
    model = Album
    template_name = 'gallery/photo-edit.html'

    def get_form_class(self):
        photo = self.get_object()
        if photo.apartment:
            if photo.apartment.for_rental:
                return EditRentalPhotoForm
            elif photo.apartment.for_sale:
                return EditSalePhotoForm
        return EditCommonPhotoForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('detail-photos', kwargs={'pk': self.object.pk})


class DeletePhotoView(DeleteView):
    model = Album
    template_name = 'gallery/photo-delete.html'
    context_object_name = 'photo'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['apartment'] = self.get_object().apartment
        return context

    def form_valid(self, form):
        photo = self.get_object()
        apartment = photo.apartment

        if apartment:
            if Album.objects.filter(apartment=apartment).count() == 1:
                if apartment.for_rental:
                    apartment.for_rental = False
                    apartment.save()
                elif apartment.for_sale:
                    apartment.for_sale = False
                    apartment.save()

        photo.delete()
        return super().form_valid(form)
