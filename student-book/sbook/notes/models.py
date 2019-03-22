from django.db import models
from sbook.models import StringIdModel
from accounts.models import User
from sbook.utils import current_user


class Quiz(StringIdModel):
    name = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="quizes",  default=current_user)


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
