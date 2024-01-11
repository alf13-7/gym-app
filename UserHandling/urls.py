from django.urls import path

from UserHandling import views

urlpatterns = [
    path("in", views.login_screen, name="login_screen"),
    path("out", views.logout_screen, name="logout_screen"),
    path("up", views.signup_screen, name="sign_up_screen")
]