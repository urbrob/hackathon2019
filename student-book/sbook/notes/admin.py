from django.contrib import admin
from notes.models import Quiz, Question, Answer


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display_links = ['pk']
    list_display = ('pk', 'name', 'created_at', 'created_by')


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display_links = ['pk']
    list_display = ('pk','description', 'quiz', 'created_at', 'created_by')

@admin.register(Answer)
class Answer(admin.ModelAdmin):
    list_display_links = ['pk']
    list_display = ('pk', 'description', 'is_valid', 'question', 'created_at', 'created_by')
