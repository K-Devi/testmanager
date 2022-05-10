from .models import *
from django.forms import ModelForm, TextInput, ModelChoiceField, Textarea


class SectionForm(ModelForm):
    courseID = ModelChoiceField(queryset=Course.objects.all(),
                                to_field_name="id")

    class Meta:
        model = Section
        fields = ['title']
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'input name'
            })
        }


class TopicForm(ModelForm):
    sectionID = ModelChoiceField(queryset=Section.objects.all(),
                                 to_field_name="id")

    class Meta:
        model = Topic
        fields = ["title"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'input name'
            })
        }


class QuestionForm(ModelForm):
    # this will show dropdown __str__ method course model is shown on html so override it
    # to_field_name this will fetch corresponding value  user_id present in course model and return it
    topicID = ModelChoiceField(queryset=Topic.objects.all(),
                               to_field_name="id")

    class Meta:
        model = Question
        fields = ['question', 'type']
        widgets = {
            'question': Textarea(attrs={'rows': 3, 'cols': 50})
        }
