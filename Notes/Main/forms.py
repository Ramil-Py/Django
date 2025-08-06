from .models import Notes
from django.forms import ModelForm, TextInput, Textarea, DateInput

class NotesForm(ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'anons', 'text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'placeholder': 'Заголовок',
                'class': 'forms'
            }),

            'anons': TextInput(attrs={
                'placeholder': 'Анонс',
                'class': 'forms'
            }),

            'text': Textarea(attrs={
                'placeholder': 'Текст',
                'class': 'forms'
            }), 

            'date': DateInput(attrs={
                'placeholder': 'Дата',
                'class': 'forms'
            })
        }

