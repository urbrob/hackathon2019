from django import forms

class QuestionDetailsForm(forms.Form):
    quiz_pk = forms.CharField(widget=forms.HiddenInput(), label='quiz_pk', max_length=100, required=False)
    question_pk = forms.CharField(widget=forms.HiddenInput(), label='description_pk', max_length=100, required=False)
    description = forms.CharField(widget=forms.TextInput(), label='description')
    answer_1 = forms.CharField(widget=forms.TextInput(), label='Answer 1',)
    answer_2 = forms.CharField(widget=forms.TextInput(), label='Answer 2',)
    answer_3 = forms.CharField(widget=forms.TextInput(), label='Answer 3', required=False)
    answer_4 = forms.CharField(widget=forms.TextInput(), label='Answer 4', required=False)


class GroupDetailsForm(forms.Form):
    description = forms.CharField(widget=forms.TextInput(), label='description')

class QuizDetailsForm(forms.Form):
    group_pk = forms.CharField(widget=forms.HiddenInput(), label='group_pk', max_length=100, required=False)
    name = forms.CharField(widget=forms.TextInput(), label='description')
