from notes.models import Quiz, Question, Answer
from rest_framework import serializers
import random


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('pk', 'description', 'is_valid', 'created_at')


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True)
    class Meta:
        model = Question
        fields = ('pk', 'description', 'created_at', 'created_by', 'answers')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        random.shuffle(data["answers"])

        return data


class QuizSerializerREST(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True)
    class Meta:
        model = Quiz
        fields = ('pk', 'name', 'created_at', 'created_by', 'questions')


class QuizSerializerListREST(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ('pk', 'name')
