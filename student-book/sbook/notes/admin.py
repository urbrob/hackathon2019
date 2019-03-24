from django.contrib import admin
from notes.models import Quiz, Question, Answer
from accounts.admin import GroupInlineAdmin


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display_links = ['pk']
    list_display = ('pk', 'name', 'created_at', 'created_by')
    inlines = [GroupInlineAdmin, ]


class AnswerInlineAdmin(admin.TabularInline):
    model = Answer
    extra = 0


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display_links = ['pk']
    list_display = ('pk','description', 'created_at', 'created_by')
    inlines = [AnswerInlineAdmin, ]


@admin.register(Answer)
class Answer(admin.ModelAdmin):
    list_display_links = ['pk']
    list_display = ('pk', 'description', 'is_valid', 'question', 'created_at', 'created_by')
