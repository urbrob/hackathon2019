from django.shortcuts import render
from rest_framework.views import APIView
from notes.models import Quiz
from rest_framework.renderers import JSONRenderer
from notes.serializers import QuizSerializer
from rest_framework.response import Response


class QuestionList(APIView):
    renderer_classes = (JSONRenderer, )

    def get(self, request, quiz_pk):
        try:
            quiz = Quiz.objects.get(id=quiz_pk)
        except Quiz.DoesNotExist:
            return Response({})
        quiz_serializer = QuizSerializer(quiz)
        return Response(quiz_serializer.data)
