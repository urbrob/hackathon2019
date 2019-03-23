from django.shortcuts import render
from rest_framework.views import APIView
from notes.models import Quiz, Group
from django.db.models import Count
from rest_framework.renderers import JSONRenderer
from notes.serializers import QuizSerializer
from rest_framework.response import Response
from django.template.loader import get_template
from django.http import Http404
from django.urls import reverse
import datetime


def quiz_start(request, group_pk, quiz_pk):
    try:
        group = Group.objects.get(id=group_pk)
    except Group.DoesNotExist:
        return Response({'error': 'Brak grupy'}, status=404)
    try:
        quiz = group.quiz_set.get(id=quiz_pk)
    except Quiz.DoesNotExist:
        return Http404('Quiz does not exist')
    questions = quiz.questions.filter(answers__is_valid=True).annotate(answers_count=Count('answers'))
    return render(request, 'quiz_start.html', {'questions': questions, 'quiz': quiz})

def quiz_display(request, group_pk, quiz_pk):
    try:
        group = Group.objects.get(id=group_pk)
    except Group.DoesNotExist:
        return Response({'error': 'Brak grupy'}, status=404)
    try:
        quiz = group.quiz_set.get(id=quiz_pk)
    except Quiz.DoesNotExist:
        return Http404('Quiz does not exist')
    quiz_serializer = QuizSerializer(quiz)
    return render(request, 'quiz_display.html', {'quiz': quiz_serializer.data})

def quizes_add_reverse_url(quizes, group_pk):
    for quiz in quizes:
        quiz.reverse_url = reverse('quiz_menu_display', args=[group_pk, quiz.pk])
        yield quiz

def group_display(request, group_pk):
    try:
        group = Group.objects.get(id=group_pk)
    except Group.DoesNotExist:
        return Response({'error': 'Brak grupy'}, status=404)
    data = {
        'quizes': quizes_add_reverse_url(group.quiz_set.all(), group.pk),
        'events': [],
        'notes': [],
    }
    return render(request, 'base_group.html', data)

def quiz_menu_display(request, group_pk, quiz_pk):
    try:
        group = Group.objects.get(id=group_pk)
    except Group.DoesNotExist:
        return Response({'error': 'Brak grupy'}, status=404)
    try:
        quiz = group.quiz_set.get(id=quiz_pk)
    except Quiz.DoesNotExist:
        return Response({'error': 'Unauthorized access'}, status=404)
    data = {
        "quiz": quiz,
        'start_url': reverse('quiz_start', args=[group_pk, quiz_pk]),
        'manage_url': reverse('quiz_display', args=[group_pk, quiz_pk])}
    return render(request, 'base_menu_quiz.html', data)


class QuestionList(APIView):
    renderer_classes = (JSONRenderer, )

    def get(self, request, quiz_pk):
        try:
            quiz = Quiz.objects.get(id=quiz_pk)
        except Quiz.DoesNotExist:
            return Response({})
        quiz_serializer = QuizSerializer(quiz)
        return Response(quiz_serializer.data)
