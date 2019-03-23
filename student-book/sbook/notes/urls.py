from django.conf.urls import url
from django.urls import path
from . import views
from accounts.views import groups_display

urlpatterns = [
    # API views
    path("api/quiz/<quiz_pk>", views.QuizDetails.as_view(), name="quiz_read"),
    path("api/groups/<user_pk>", views.UserGroupsList.as_view(), name="groups_read"),
    path("api/quizes/<user_pk>/<group_pk>", views.QuizList.as_view(), name="quizes_read"),

    # APP views
	path("groups", groups_display, name="groups"),
	path("group/<group_pk>", views.group_display, name='group_display'),
	path("group/<group_pk>/<quiz_pk>", views.quiz_menu_display, name='quiz_menu_display'),
	path("group/<group_pk>/<quiz_pk>/manage", views.quiz_display, name="quiz_display"),
	path("group/<group_pk>/<quiz_pk>/quiz_start", views.quiz_start, name='quiz_start'),
]
