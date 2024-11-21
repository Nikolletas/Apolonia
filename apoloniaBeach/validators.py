import os

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class NameLetterValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = "Name can only contain letters and spaces."
        else:
            self.__message = value

    def __call__(self, value: str, *args, **kwargs):
        for char in value:
            if not (char.isalpha() or char.isspace()):
                raise ValidationError(self.message)


@deconstructible
class AlphaNumericValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = "Name can only contain letters and numbers."
        else:
            self.__message = value

    def __call__(self, value: str, *args, **kwargs):
        for char in value:
            if not (char.isalpha() or char.isdigit()):
                raise ValidationError(self.message)


@deconstructible
class NumericValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = "Phone number can only contain digits."
        else:
            self.__message = value

    def __call__(self, value: str, *args, **kwargs):
        for char in value:
            if not char.isdigit():
                raise ValidationError(self.message)


def file_validator(file):
    max_size_mb = 5
    allowed_image_extensions = ['jpg', 'jpeg', 'png', 'gif']
    allowed_document_extensions = ['pdf', 'doc', 'docx', 'txt']
    allowed_extensions = allowed_image_extensions + allowed_document_extensions

    if file.size > max_size_mb * 1024 * 1024:
        raise ValidationError(f"The file size should not exceed {max_size_mb} MB.")

    ext = os.path.splitext(file.name)[1][1:].lower()
    if ext not in allowed_extensions:
        raise ValidationError(f"Allowed file types are: {', '.join(allowed_extensions)}.")

