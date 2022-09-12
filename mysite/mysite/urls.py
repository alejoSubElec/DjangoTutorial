from django.contrib import admin
from django.urls import path
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("apidjrst/", include("quickstart.urls")),
    path("snippets/", include("snippets.urls")),
    path('admin/', admin.site.urls),
     path("api-auth/", include("rest_framework.urls")),
]

