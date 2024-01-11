from django.urls import path

from MainApp import views

urlpatterns = [
    path("", views.beginning_page_redirect, name="beginning_page_redirect"),
]