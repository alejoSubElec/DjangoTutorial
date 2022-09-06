from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("34:question_id", views.detail, name="detail"),
    path("34", views.results, name="results"),
    path("34", views.vote, name="vote")
]