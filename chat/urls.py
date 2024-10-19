from django.urls import path, include
# from chat import views as chat_views
from . import views

from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path("", views.chatPage, name="chat-page"),          # Home or Chat Page
    path("login/", views.login_view, name="login-user"),
    path("logout/", views.login_view, name="logout-user"),
]
