from django import forms
from django.db import transaction


class FormService(forms.Form):
    """
    This class is used to validate the form data.
    """

    def service_clean(self):
        if self.is_valid():
            if (
                self.cleaned_data.get("username")
                and self.cleaned_data.get("password")
                and self.cleaned_data.get("email_address") is None
            ):
                raise NotImplementedError()

    @classmethod
    def execute(cls, inputs, files=None, **kwargs):
        instance = cls(inputs, files, **kwargs)
        instance.service_clean()

        # We have this in a transaction for rollback purposes
        with transaction.atomic():
            return instance.process()

    def process(self):
        raise NotImplementedError()
