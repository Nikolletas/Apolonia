from django import forms

from apoloniaBeach.common.models import AssociationDocument


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
