from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path("question/<quiz_pk>", views.QuestionList.as_view(), name="quiz_read"),
]
