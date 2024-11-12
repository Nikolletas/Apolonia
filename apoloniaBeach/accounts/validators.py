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

