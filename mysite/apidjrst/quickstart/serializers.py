from dataclasses import fields
from django.contrib.auth.models import Question, Choice
from rest_framework import serializers

class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ["__all__"]

class QuestionSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ["__all__"]

class ChoiceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Choice
        fields = ["__all__"]

class ChoiceSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ["__all__"]