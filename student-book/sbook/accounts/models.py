from django.contrib.auth.models import AbstractUser
from sbook.models import StringIdModel
from django.db import models
from sbook.utils import current_user


class User(StringIdModel, AbstractUser):
    pass


class Group(StringIdModel):
    OWNER = 'owner'
    MODERATOR = 'moderator'
    USER = 'user'
    STATUSES = (
        (OWNER, 'Owner'),
        (MODERATOR, 'Moderator'),
        (USER, 'User'),
    )

    name = models.CharField(max_length=250)
    users = models.ManyToManyField(User, through='accounts.Membership')
    status = models.CharField(choices=STATUSES, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name="created_groups", default=current_user)

class Membership(StringIdModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='group_memberships')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='memberships')
    created_at = models.DateTimeField(auto_now_add=True)
