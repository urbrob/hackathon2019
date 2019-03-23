from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
	path("question/<quiz_pk>", views.QuestionList.as_view(), name="quiz_read"),
	#path("question_display/<quiz_pk>", views.quiz_display, name="quiz_display"),
	path("group/<group_pk>", views.group_display, name='group_display'),
	path("group/<group_pk>/<quiz_pk>", views.quiz_menu_display, name='quiz_menu_display'),
]
