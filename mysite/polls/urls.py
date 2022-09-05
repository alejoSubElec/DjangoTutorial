from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("5", views.detail, name="detail"),
    path("5", views.results, name="results"),
    path("5", views.vote, name="vote")
]