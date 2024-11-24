from django.contrib.auth import get_user_model
from django.shortcuts import redirect, render
from apoloniaBeach.houses.forms import EditApartmentForm, AddApartmentForm, EditApartmentOwnerForm
from apoloniaBeach.houses.models import Apartment, House

UserModel = get_user_model()


def apartments(request):
    houses = House.objects.all().order_by('name')

    def extract_number(value):
        digits = ''.join(char for char in value if char.isdigit())
        return int(digits) if digits else float('inf')

    for house in houses:
        house.apartments_sorted = sorted(
            house.apartments.all(),
            key=lambda apartment: (extract_number(apartment.number), apartment.number)
        )

    if request.user.is_superuser or request.user.is_staff:
        context = {'houses': houses}
        return render(request, 'houses/apartments.html', context)
    else:
        return redirect('home')


def add_apartment(request):
    form = AddApartmentForm(request.POST or None, request.FILES or None)

    if request.user.is_superuser:
        if form.is_valid():
            form.save()
            return redirect('apartments')

    context = {'form': form}

    return render(request, 'houses/add-apartment.html', context)


def details_apartment(request, pk):
    apartment = Apartment.objects.get(pk=pk)
    context = {
        'apartment': apartment
    }

    return render(request, 'houses/details-apartment.html', context)


def edit_apartment_view(request, pk):
    apartment = Apartment.objects.get(pk=pk)
    form = EditApartmentForm(request.POST or None, request.FILES or None, instance=apartment)
    if not request.user.is_superuser:
        form = EditApartmentOwnerForm(request.POST or None, request.FILES or None, instance=apartment)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            if not request.user.is_superuser:
                return redirect('profile-details', request.user.pk)
            else:
                return redirect('details-apartment', pk)

    context = {
        'apartment': apartment,
        'form': form,
    }
    return render(request, 'houses/edit-apartment.html', context)


def delete_apartment_view(request, pk):
    apartment = Apartment.objects.get(pk=pk)
    if request.method == 'POST':
        if request.user.is_superuser:
            apartment.delete()
            return redirect('apartments')
        return redirect('home')
    context = {
        'apartment': apartment
    }

    return render(request, 'houses/delete-apartment.html', context)