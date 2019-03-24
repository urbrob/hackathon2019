from django import forms

class QuestionDetailsForm(forms.Form):
    quiz_pk = forms.CharField(widget=forms.HiddenInput(attrs={'class':'form-control'}), label='quiz_pk', max_length=100, required=False)
    question_pk = forms.CharField(widget=forms.HiddenInput(attrs={'class':'form-control'}), label='description_pk', max_length=100, required=False)
    description = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='Pytanie')
    answer_1 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='Odpowiedź 1',)
    answer_2 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='Odpowiedź 2',)
    answer_3 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='Odpowiedź 3', required=False)
    answer_4 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='Odpowiedź 4', required=False)


class GroupDetailsForm(forms.Form):
    description = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='Description')

class QuizDetailsForm(forms.Form):
    group_pk = forms.CharField(widget=forms.HiddenInput(attrs={'class':'form-control'}), label='group_pk', max_length=100, required=False)
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), label='Nazwa')
