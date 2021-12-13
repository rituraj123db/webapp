from django import forms
from django.shortcuts import render

from user_management.base_controllers import FormService
from user_management.form import UserForm
from user_management.models import MessageData, User


class UserController(FormService):
    """
    This class inherit with form-service from base controller module
    """

    def process(self):
        data = self.data.get("request")
        if data.method == "POST":
            if data.POST.get("username") and data.POST.get("password"):
                user = User()
                if user.username == data.POST.get("username"):
                    return render(data, "dashboard.html")
                user.password = data.POST.get("password")
                user.save()
                return render(data, "login.html")
        else:
            return render(data, "dashboard.html", {"form": UserForm()})


class DashBoardController(forms.Form):
    """
    This class inherit with form-service from base controller module
    """

    def process(self):
        data = self.data.get("request")
        user = MessageData()
        return render(data, "dashboard.html", {"form": user})
