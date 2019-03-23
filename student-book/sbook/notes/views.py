from django.shortcuts import render
from rest_framework.views import APIView
from notes.models import Quiz, Group
from django.db.models import Count
from rest_framework.renderers import JSONRenderer
from accounts.serializers import GroupSerializerREST
from notes.serializers import QuizSerializerREST, QuizSerializerListREST,  QuestionSerializer
from rest_framework.response import Response
from django.template.loader import get_template
from notes.forms import QuestionDetailsForm, GroupDetailsForm, QuizDetailsForm
from django.http import Http404
from rest_framework import permissions
from django.urls import reverse
from django.db.models import Q
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
    questions_serializers = QuestionSerializer(quiz.questions.all(), many=True)
    #import pdb; pdb.set_trace()
    return render(request, 'quiz_start.html', {'questions': questions_serializers.data, 'quiz': quiz})

def quiz_display(request, group_pk, quiz_pk):
    try:
        group = Group.objects.get(id=group_pk)
    except Group.DoesNotExist:
        return Response({'error': 'Brak grupy'}, status=404)
    try:
        quiz = group.quiz_set.get(id=quiz_pk)
    except Quiz.DoesNotExist:
        return Http404('Quiz does not exist')
    quiz_serializer = QuizSerializerREST(quiz)
    return render(request, 'quiz_display.html', {'quiz': quiz_serializer.data})

def quizes_add_reverse_url(quizes, group_pk):
    for quiz in quizes:
        quiz.reverse_url = reverse('quiz_menu_display', args=[group_pk, quiz.pk])
        yield quiz


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


class UserGroupsListREST(APIView):
    renderer_classes = (JSONRenderer, )

    def get(self, request, user_pk):
        try:
            group = Group.objects.filter(users=user_pk).distinct()
        except Group.DoesNotExist:
            return Response({})
        group_serializer = GroupSerializerREST(group, many=True)
        return Response(group_serializer.data)


class QuizListREST(APIView):
    renderer_classes = (JSONRenderer, )

    def get(self, request, user_pk, group_pk):
        try:
            group = Group.objects.filter(id=group_pk, users=user_pk).distinct()[0]
            quizes = group.quiz_set.all().distinct()
        except (Quiz.DoesNotExist, IndexError):
            return Response({})
        quiz_serializer = QuizSerializerListREST(quizes, many=True)
        return Response(quiz_serializer.data)


class QuizDetails(APIView):
    renderer_classes = (JSONRenderer, )

    def get(self, request, quiz_pk):
        try:
            quiz = Quiz.objects.get(id=quiz_pk)
        except Quiz.DoesNotExist:
            return Response({})
        quiz_serializer = QuizSerializerREST(quiz)
        return Response(quiz_serializer.data)


class QuestionDetails(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request, group_pk, quiz_pk):
        try:
            group = Group.objects.get(id=group_pk)
        except Group.DoesNotExist:
            return Response({'error': 'Brak grupy'}, status=404)
        try:
            quiz = group.quiz_set.get(id=quiz_pk)
        except Quiz.DoesNotExist:
            return Http404('Quiz does not exist')
        quiz_serializer = QuizSerializerREST(quiz)
        form = QuestionDetailsForm()
        return render(request, 'quiz_display.html', {'form': form, 'quiz': quiz_serializer.data})

    def post(self, request):
        data = request.data.dict()
        answer_list = [data['answer_1'], data['answer_2'], data['answer_3'], data['answer_4']]
        if data.get('question_pk'):
            question = Question.objects.get(id='question_pk').update_answers(answer_list, data['description'])
        else:
            Question.create_with_answers(data['description'], answer_list)
        quiz = group.quiz_set.get(id=quiz_pk)
        quiz_serializer = QuizSerializerREST(quiz)
        form = QuestionDetailsForm()
        return render(request, 'quiz_display.html', {'form': form, 'quiz': quiz_serializer.data})


class GroupsList(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        my_groups = Group.objects.filter(users=request.user).distinct()
        all_groups = Group.objects.filter(~Q(id__in=my_groups.values_list('id', flat=True)))
        form = GroupDetailsForm()
        return render(request, 'accounts/groups.html', {'my_groups': my_groups, 'all_groups': all_groups, 'form': form})

    def post(self, request):
        data = request.data.dict()
        group = Group.objects.create(created_by=request.user, name=data['name'])
        Membership.objects.create(user=request.user, group=group)
        my_groups = Group.objects.filter(users=request.user).distinct()
        all_groups = Group.objects.filter(~Q(id__in=my_groups.values_list('id', flat=True)))
        form = GroupDetailsForm()
        return render(request, 'accounts/groups.html', {'my_groups': my_groups, 'all_groups': all_groups, 'form': form})


class QuizList(APIView):
    permissions_classes = (permissions.AllowAny,)

    def get(self, request, group_pk):
        try:
            group = Group.objects.get(id=group_pk)
        except Group.DoesNotExist:
            return Response({'error': 'Brak grupy'}, status=404)
        form = QuizDetailsForm()
        data = {
            'quizes': quizes_add_reverse_url(group.quiz_set.all(), group.pk),
            'events': [],
            'notes': [],
            'form': form,
        }
        return render(request, 'base_group.html', data)

    def post(self, request):
        data = request.data.dict()
        group = Group.objects.get(id=data['group_pk'])
        quiz = Quiz.objects.create(created_by=request.user, name=data['name'])
        quiz.groups.add(group)
        try:
            group = Group.objects.get(id=group_pk)
        except Group.DoesNotExist:
            return Response({'error': 'Brak grupy'}, status=404)
        form = QuizDetailsForm()
        data = {
            'quizes': quizes_add_reverse_url(group.quiz_set.all(), group.pk),
            'events': [],
            'notes': [],
            'form': form,
        }
        return render(request, 'base_group.html', data)
