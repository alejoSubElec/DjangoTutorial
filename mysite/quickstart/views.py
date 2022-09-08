from django.shortcuts import render
from polls.models import Question, Choice
from rest_framework import viewsets
from rest_framework import permissions
from quickstart.serializers import QuestionSerializer, QuestionSerializer2, ChoiceSerializer, ChoiceSerializer2

class QuestionViewSet(viewsets.ModelViewSet):
    "API endpoint"
    queryset = Question.objects.all().order_by("-pub_date")
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]

class ChoiceViewSet(viewsets.ModelViewSet):
    "API endpoint"
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    permission_classes = [permissions.IsAuthenticated]
