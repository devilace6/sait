from .models import Articles
from django.forms import ModelForm, TextInput, DateInput, Textarea, CharField
import datetime
from tinymce.widgets import TinyMCE

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title',
                  'anons',
                  'full_text',
                  'date']
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
            'placeholder': 'Текст статьи', 'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})
            }),
            "date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации',
                'value': datetime.datetime.now().strftime("%d.%m.%Y")
            })
        }