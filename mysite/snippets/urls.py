from django.urls import path, include 
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path("", views.SnippetList.as_view()),
    path("<int:pk>/", views.SnippetList.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
   
]

urlpatterns = format_suffix_patterns(urlpatterns)

