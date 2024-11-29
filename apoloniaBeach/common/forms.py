from django import forms

from apoloniaBeach.common.models import AssociationDocument, Announcement


class AssociationDocumentBaseForm(forms.ModelForm):
    class Meta:
        model = AssociationDocument
        exclude = ['upload_date', 'uploaded_by']

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Some title'}),
        }
        labels = {
            'title': 'Title:',
            'document_type': 'Document type:',
            'file': 'Upload file:'
        }


class AssociationDocumentAddForm(AssociationDocumentBaseForm):
    pass


class AssociationDocumentEditForm(AssociationDocumentBaseForm):
    pass


class AnnouncementBaseForm(forms.ModelForm):
    class Meta:
        model = Announcement
        exclude = ['posted_by', 'date_posted']

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Some title'}),
            'content': forms.Textarea(attrs={'placeholder': 'Some content'}),
        }

        labels = {
            'title': 'Please, write title:',
            'content': 'Please, write your announcement:',
            'category': 'Please, choose a category',
        }


class AnnouncementAddForm(AnnouncementBaseForm):
    pass


class AnnouncementEditForm(AnnouncementBaseForm):
    pass
