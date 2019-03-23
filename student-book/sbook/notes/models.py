from django.db import models
from sbook.models import StringIdModel
from accounts.models import User, Group
from sbook.utils import current_user
from django.apps import apps


class Quiz(StringIdModel):
    name = models.CharField(max_length=250)
    groups = models.ManyToManyField(Group)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="quizes",  default=current_user)

    @classmethod
    def create_with_answers(cls, description, user, answer_list, group):
        question = Question.objects.create(description=description, created_by=user)
        Answer = apps.get_model(app_label='notes', model_name='Answer')
        for index, answer in enumerate(answer_list):
            Answer.objects.create(
                description=description,
                is_valid=index is 1,
                question=question,
                created_by=user
            )
        question.groups.add(group)
        question.save()

    def update_answers(self, answer_list, description):
        for index, answer in enumerate(self.answers.all().order_by('-created_at')):
            answer.description = answer_list[index]
            answer.save()
        question.description = description
        question.save()


class Question(StringIdModel):
    description = models.CharField(max_length=250)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="questions",  default=current_user)


class Answer(StringIdModel):
    description = models.CharField(max_length=250)
    is_valid = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="answers",  default=current_user)
