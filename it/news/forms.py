from .models import Articles, Comments
from django.forms import ModelForm, TextInput, DateInput, Textarea, CharField, ModelChoiceField, ChoiceField, Select
import datetime

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title',
                  'anons',
                  'full_text',
                  'date', 'category']
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            "anons": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи',
            }),
            "date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации',
                'value': datetime.datetime.now().strftime("%d.%m.%Y"),
            }),
            "category": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Категории',
            }),
        }

# class CommentForm(ModelForm):
#     class Meta:
#         model = Comments
#         fields = ['text']
#     def __init__(self,*args,**kwargs):
#         super().__init__(*args,**kwargs)
#         for field in self.fields:
#             self.fields[field].widget.attrs['class'] = 'form-control'

class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['text']
        widgets = {
            "text": Textarea(attrs={
                'rows':5,
                'class': 'form-control',
                'placeholder': 'Текст комментария'
            }),
        }