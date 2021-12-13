from django import forms

from user_management.models import MessageData, User


class UserForm(forms.ModelForm):
    """
    This is django form to insert data in model.
    """

    class Meta:
        model = User
        fields = ["username", "password"]


class UpdateUserForm(forms.ModelForm):
    """
    This is django form to insert data in model.
    """

    class Meta:
        model = User
        fields = ["username"]


class ChangePasswordForm(forms.ModelForm):
    """
    This is django form to insert data in model.
    """

    class Meta:
        model = User
        fields = ["password"]


class MessageForm(forms.ModelForm):
    """
    This is django form to insert data in model.
    """

    class Meta:
        model = MessageData
        fields = ["message", "user"]
