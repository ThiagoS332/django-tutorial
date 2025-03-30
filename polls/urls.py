from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("test/<int:number>", views.test_view, name="show_request")
]