from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views.generic import ListView

from apoloniaBeach.accounts.models import MyUser
from apoloniaBeach.albums.models import Album
from apoloniaBeach.common.forms import AssociationDocumentAddForm, AssociationDocumentEditForm
from apoloniaBeach.common.models import AssociationDocument

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


def documents(request):
    return render(request, 'documents/documents.html')


def home_book(request):
    users = UserModel.objects.all().order_by('profile__owner_by')
    users_per_page = 6
    paginator = Paginator(users, users_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'users': users,
        'page_obj': page_obj,
    }

    return render(request, 'documents/home-book.html', context)


def association_documents(request):
    all_documents = AssociationDocument.objects.all().order_by('document_type', '-upload_date')
    documents_per_page = 2
    paginator = Paginator(all_documents, documents_per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'all_documents': all_documents,
        'page_obj': page_obj,
    }

    return render(request, 'documents/all-documents.html', context)


def association_document_add(request):
    form = AssociationDocumentAddForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            document = form.save(commit=False)
            document.uploaded_by = request.user
            document.save()
            return redirect('all-documents')

    context = {
        'form': form,
    }

    return render(request, 'documents/document-add.html', context)


def association_document_edit(request, pk):
    document = AssociationDocument.objects.get(pk=pk)
    form = AssociationDocumentEditForm(request.POST or None, request.FILES or None, instance=document)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

            return redirect('all-documents')

    context = {
        'form': form,
    }

    return render(request, 'documents/document-edit.html', context)


def association_document_delete(request, pk):
    document = AssociationDocument.objects.get(pk=pk)
    if request.method == 'POST':
        document.delete()
        return redirect('all-documents')

    context = {
        'document': document,
    }

    return render(request, 'documents/document-delete.html', context)