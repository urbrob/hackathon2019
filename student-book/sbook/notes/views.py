from django.shortcuts import render
from rest_framework.views import APIView
from notes.models import Quiz, Group
from rest_framework.renderers import JSONRenderer
from notes.serializers import QuizSerializer
from rest_framework.response import Response
from django.template.loader import get_template
from django.http import Http404
from django.urls import reverse
import datetime


def quiz_display(request, group_pk, quiz_pk):
    try:
        group = Group.objects.filter(id=group_pk, users=request.user)[0]
    except IndexError:
        return Response({'error': 'Unauthorized access'}, status=404)
    try:
        quiz = group.quiz_set.get(id=quiz_pk)
    except Quiz.DoesNotExist:
        return Http404('Quiz does not exist')
    quiz_serializer = QuizSerializer(quiz)
    return render(request, 'quiz_display.html', {'quiz': quiz_serializer.data})


def group_display(request, group_pk):
    try:
        group = Group.objects.filter(id=group_pk, users=request.user)[0]
    except IndexError:
        return Response({'error': 'Unauthorized access'}, status=404)
    data = {
        'quizes': group.quiz_set.all(),
        'events': [],
        'notes': [],
    }
    return render(request, 'base_group.html', data)

def quiz_menu_display(request, group_pk, quiz_pk):
    try:
        group = Group.objects.filter(id=group_pk, users=request.user)[0]
    except IndexError:
        return Response({'error': 'Unauthorized access'}, status=404)
    try:
        quiz = group.quiz_set.get(id=quiz_pk)
    except Quiz.DoesNotExist:
        return Response({'error': 'Unauthorized access'}, status=404)
    return render(request, 'base_menu_quiz.html', {"quiz": quiz, 'manage_url': reverse('quiz_display', args=[group_pk, quiz_pk])})


class QuestionList(APIView):
    renderer_classes = (JSONRenderer, )

    def get(self, request, quiz_pk):
        try:
            quiz = Quiz.objects.get(id=quiz_pk)
        except Quiz.DoesNotExist:
            return Response({})
        quiz_serializer = QuizSerializer(quiz)
        return Response(quiz_serializer.data)
