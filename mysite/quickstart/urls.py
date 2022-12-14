from django.urls import include, path
from rest_framework import routers
from quickstart import views

router = routers.DefaultRouter()
router.register(r"questions", views.QuestionViewSet)
router.register(r"choices", views.ChoiceViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api-auth", include("rest_framework.urls", namespace="rest_framework"))
]

