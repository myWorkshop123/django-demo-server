from django.urls import path

from . import views

urlpatterns = [
    path("<int:poll_id>", views.detail, name="index"),
]