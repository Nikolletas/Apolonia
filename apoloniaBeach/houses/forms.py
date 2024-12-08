from django import forms

from apoloniaBeach.houses.models import Apartment, House


class HouseBaseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = '__all__'


class AddHouseForm(HouseBaseForm):
    pass


class EditHouseForm(HouseBaseForm):
    pass


class ApartmentBaseForm(forms.ModelForm):
    class Meta:
        model = Apartment
        fields = '__all__'

        labels = {
            'number': 'Apartment number',
            'apartment_area': 'Apartment area',
            'common_parts_of_the_building': 'Common parts',
            'for_rental': 'If apartment is for rental, please check:',
            'for_sale': 'If apartment is for sale, please check:',
        }


class AddApartmentForm(ApartmentBaseForm):
    pass


class EditApartmentForm(ApartmentBaseForm):
    class Meta(ApartmentBaseForm.Meta):
        exclude = ['house']


class EditApartmentOwnerForm(ApartmentBaseForm):
    class Meta(ApartmentBaseForm.Meta):
        exclude = ['house', 'number', 'apartment_area', 'common_parts_of_the_building']




