# Create your views here.
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, View

from user_management.controllers import DashBoardController, UserController
from user_management.form import MessageForm, UpdateUserForm, UserForm
from user_management.models import MessageData, User


def login_view(request):
    """
    This function are user to create the user with login page.
    """
    return UserController.execute({"request": request})


class HomeView(View):
    @staticmethod
    def get(request):
        return render(request, "index.html")


class LoginView(View):
    @staticmethod
    def get(request):
        user_form = UserForm(request.POST)
        return render(request, "login.html", {"user_form": user_form})

    @staticmethod
    def post(request):
        try:
            user_object = User.objects.get(username=request.POST.get("username"))
            if user_object:
                return HttpResponseRedirect("/dashboard/")
        except User.DoesNotExist:
            form_user = UserForm(request.POST)
            if form_user.is_valid():
                form_user.save()
                return HttpResponseRedirect("/dashboard/")


class DashboardView(ListView):
    model = MessageData
    template_name = "dashboard.html"


class CreateMessage(CreateView, SuccessMessageMixin):
    breakpoint()
    model = MessageData
    form_class = MessageForm
    success_url = reverse_lazy("message_list")
    template_name = "message_form.html"
    success_message = "Appointment successfully created!."


class MessageListView(ListView):
    model = MessageData
    template_name = "message_list.html"
    context_object_name = "apps"

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.all()


class ForgotPassword(CreateView):
    @staticmethod
    def update(request):
        try:
            user_object = User.objects.get(username=request.POST.get("username"))
            if user_object:
                if user_object.is_valid():
                    user_object.save()
                return render(request, "login.html", {"user_form": "user_form"})

            return HttpResponseRedirect("/dashboard/")
        except User.DoesNotExist:
            return HttpResponse(
                {f"User Does not exit with {request.POST.get('username')} usernname."}
            )
