from django.db import models
from sbook.models import StringIdModel
from accounts.models import User, Group
from sbook.utils import current_user
from django.apps import apps
from django.db.models import Q


class Quiz(StringIdModel):
    name = models.CharField(max_length=250)
    groups = models.ManyToManyField(Group)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="quizes", default=current_user
    )


class Question(StringIdModel):
    description = models.CharField(max_length=250)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="questions")
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="questions", default=current_user
    )

    @classmethod
    def create_with_answers(cls, description, user, answer_list, quiz_id):
        quiz = Quiz.objects.get(id=quiz_id)
        question = cls.objects.create(
            description=description, created_by=user, quiz=quiz
        )
        question = question.update_answers(answer_list, description)
        return question

    def update_answers(self, answer_list, description):
        for index, answer in enumerate(self.answers.all().order_by("-created_at")):
            answer.description = answer_list[index]
            answer.save()
        self.description = description
        self.save()
        return self


class Answer(StringIdModel):
    description = models.CharField(max_length=250, null=True, blank=True)
    is_valid = models.BooleanField(default=False)
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="answers"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="answers", default=current_user
    )

    def save(self, *args, **kwargs):
        if self.question.answers.filter(~Q(id=self.id)).count() < 5:
            super().save(*args, **kwargs)
