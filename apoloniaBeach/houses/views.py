from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.shortcuts import redirect, render

from apoloniaBeach.decorators import user_is_apartment_owner
from apoloniaBeach.houses.forms import EditApartmentForm, AddApartmentForm, EditApartmentOwnerForm, AddHouseForm, \
    EditHouseForm
from apoloniaBeach.houses.models import Apartment, House

UserModel = get_user_model()


@login_required
def houses(request):
    houses = House.objects.all().order_by('name')
    if request.user.is_superuser or request.user.is_staff:
        context = {'houses': houses}
        return render(request, 'houses/houses.html', context)
    else:
        return redirect('home')




@login_required
def add_house(request):
    form = AddHouseForm(request.POST or None)

    if request.user.is_superuser:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                return redirect('houses')

    else:
        return render(
            request,
            '403.html',
            {"message": "You are not permissions to do this."},
            status=403
        )

    context = {'form': form}

    return render(request, 'houses/add-house.html', context)



@login_required
def edit_house(request, pk):
    house = House.objects.get(pk=pk)
    form = EditHouseForm(request.POST or None, instance=house)

    if request.user.is_superuser:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                return redirect('houses')

    else:
        return render(
            request,
            '403.html',
            {"message": "You are not permissions to do this."},
            status=403
        )

    context = {'form': form}

    return render(request, 'houses/edit-house.html', context)



@user_is_apartment_owner
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


@login_required
def add_apartment(request):
    form = AddApartmentForm(request.POST or None)

    if request.user.is_superuser:
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                return redirect('apartments')

    else:
        return render(
            request,
            '403.html',
            {"message": "You are not permissions to do this."},
            status=403
        )

    context = {'form': form}

    return render(request, 'houses/add-apartment.html', context)


@user_is_apartment_owner
def details_apartment(request, pk):
    apartment = Apartment.objects.get(pk=pk)
    if apartment.owner == request.user or request.user.is_staff:
        context = {
            'apartment': apartment
        }

        return render(request, 'houses/details-apartment.html', context)


@login_required
def edit_apartment(request, pk):
    apartment = Apartment.objects.get(pk=pk)
    form = EditApartmentOwnerForm(request.POST or None, instance=apartment)
    manager_group = Group.objects.get(name="Manager")

    if manager_group in request.user.groups.all() or request.user.is_superuser:
        form = EditApartmentForm(request.POST or None, instance=apartment)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('details-apartment', pk)

    context = {
        'apartment': apartment,
        'form': form,
    }
    return render(request, 'houses/edit-apartment.html', context)


@login_required
def delete_apartment(request, pk):
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
