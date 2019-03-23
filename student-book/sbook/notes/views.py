from django.shortcuts import render
from rest_framework.views import APIView
from notes.models import Quiz
from rest_framework.renderers import JSONRenderer
from notes.serializers import QuizSerializer
from rest_framework.response import Response
from django.template.loader import get_template
from django.http import HttpResponse
import datetime

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

def quiz_display(request, quiz_pk):
    try:
        quiz = Quiz.objects.get(id=quiz_pk)
    except Quiz.DoesNotExist:
        return Response({})
    quiz_serializer = QuizSerializer(quiz)
    html = get_template('quiz_display.html').render({'quiz': quiz_serializer.data})
    return HttpResponse(html)


class QuestionList(APIView):
    renderer_classes = (JSONRenderer, )

    def get(self, request, quiz_pk):
        try:
            quiz = Quiz.objects.get(id=quiz_pk)
        except Quiz.DoesNotExist:
            return Response({})
        quiz_serializer = QuizSerializer(quiz)
        return Response(quiz_serializer.data)
