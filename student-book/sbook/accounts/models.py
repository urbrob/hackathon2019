from django.contrib.auth.models import AbstractUser
from sbook.models import StringIdModel


class User(StringIdModel, AbstractUser):
    pass
