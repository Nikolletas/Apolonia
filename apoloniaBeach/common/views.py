from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import ListView

from apoloniaBeach.accounts.models import MyUser
from apoloniaBeach.albums.models import Album

UserModel = get_user_model()


def home_page(request):
    user = UserModel
    all_our_photos = Album.objects.all().order_by('photo_type')
    photos_per_page = 2

    paginator = Paginator(all_our_photos, photos_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }

    if request.user.is_authenticated:
        return render(request, 'common/our-home-page.html', context)
    else:
        return render(request, 'common/home-page.html')


def rules(request):
    return render(request, 'common/rules.html')


def contacts(request):
    users = MyUser.objects.filter(is_staff=True)

    context = {
        'users': users,
    }

    return render(request, 'common/contacts.html', context)



