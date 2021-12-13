from django.urls import path

from user_management.views import (
    CreateMessage,
    DashboardView,
    ForgotPassword,
    HomeView,
    LoginView,
    MessageListView,
)

urlpatterns = [
    path("home/", HomeView.as_view(), name="home_view"),
    path("login_user/", LoginView.as_view(), name="login_user"),
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    path("message_create/", CreateMessage.as_view(), name="message_create"),
    path("message_list/", MessageListView.as_view(), name="message_list"),
    path("forgot_password/", ForgotPassword, name="forgot_password"),
]
