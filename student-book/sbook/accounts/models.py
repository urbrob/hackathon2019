from django.contrib.auth.models import AbstractUser
from sbook.models import StringIdModel


class CustomUser(StringIdModel, AbstractUser):
    pass
