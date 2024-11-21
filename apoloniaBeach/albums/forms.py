from django import forms

from apoloniaBeach.albums.models import Album
from apoloniaBeach.houses.models import Apartment


class AddCommonPhotoForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['photo', 'description', ]

        widgets = {
            'description': forms.Textarea(attrs={'placeholder': 'Write something nice about the photo'}),
        }
        labels = {
            'photo': 'Photo Upload',
            'description': 'Photo Description',
        }


class AddRentalPhotoForm(forms.ModelForm):
    apartment = forms.ModelChoiceField(
        queryset=Apartment.objects.all(),
        required=True,
    )

    class Meta:
        model = Album
        fields = ['photo', 'description', 'price_per_night', 'apartment', 'currency']

        widgets = {
            'description': forms.Textarea(attrs={'placeholder': 'Write something nice about the photo'}),
            'price_per_night': forms.NumberInput(attrs={'placeholder': 'Enter price for night'}),
        }
        labels = {
            'photo': 'Photo Upload',
            'description': 'Photo Description',
            'price': 'Sale Price',
            'apartment': 'Please, choose an apartment',
            'currency': 'Please, choose an currency',
        }


class AddSalePhotoForm(forms.ModelForm):
    apartment = forms.ModelChoiceField(
        queryset=Apartment.objects.all(),
        required=True,
    )

    class Meta:
        model = Album
        fields = ['photo', 'description', 'price', 'apartment', 'currency']

        widgets = {
            'description': forms.Textarea(attrs={'placeholder': 'Write something nice about the photo'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Enter price'}),
        }
        labels = {
            'photo': 'Photo Upload',
            'description': 'Photo Description',
            'price': 'Sale Price',
            'apartment': 'Please, choose an apartment',
            'currency': 'Please, choose an currency',
        }


class EditCommonPhotoForm(AddCommonPhotoForm):
    pass


class EditRentalPhotoForm(AddRentalPhotoForm):
    pass


class EditSalePhotoForm(AddSalePhotoForm):
    pass
