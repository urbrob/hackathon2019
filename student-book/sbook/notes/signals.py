from notes.models import Question, Answer
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Question)
def add_answers(sender, instance, created, **kwargs):
    if created:
        for index, answer in enumerate(["", "", "", ""]):
            Answer.objects.create(
                description=answer,
                is_valid=index is 3,
                question=instance,
                created_by=instance.created_by,
            )
