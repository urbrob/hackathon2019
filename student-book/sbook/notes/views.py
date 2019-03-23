from django.shortcuts import render
from rest_framework.views import APIView
from notes.models import Quiz, Group
from rest_framework.renderers import JSONRenderer
from notes.serializers import QuizSerializer
from rest_framework.response import Response
from django.template.loader import get_template
from django.http import HttpResponse
import datetime


def quiz_display(request, quiz_pk):
    try:
        quiz = Quiz.objects.get(id=quiz_pk)
    except Quiz.DoesNotExist:
        return Response({})
    quiz_serializer = QuizSerializer(quiz)
    html = get_template('quiz_display.html').render({'quiz': quiz_serializer.data})
    return HttpResponse(html)

def group_display(request, group_pk):
    try:
        group = Group.objects.get(id=quiz_pk, users=request.user)
    except Quiz.DoesNotExist:
        return Response({'error': 'Unauthorized access'}, status=404)
    data = {
        'quizes': group.quiz_set.all(),
        'events': [],
        'notes': [],
    }
    return render(request, 'base_group.html', data)


class QuestionList(APIView):
    renderer_classes = (JSONRenderer, )

    def get(self, request, quiz_pk):
        try:
            quiz = Quiz.objects.get(id=quiz_pk)
        except Quiz.DoesNotExist:
            return Response({})
        quiz_serializer = QuizSerializer(quiz)
        return Response(quiz_serializer.data)
