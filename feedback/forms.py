from django import forms
from .models import *

# class FeedbackForm(forms.Form):
#     name = forms.CharField(label='Имя', max_length=7, min_length=2, error_messages={
#         'max_length': 'Слишком много симваолов',
#         'min_length': 'Слишком мало симваолов',
#         'required': 'Хотя бы 1 символ',
#     })
#     surname = forms.CharField()
#     feedback = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 20}))
#     rating = forms.IntegerField(label='Рейтинг', max_value=5, min_value=1)


from django import forms
from .models import *

# Класс ModelForm
class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        # fields = ['name', 'surname']
        fields = '__all__'
        # exclude = ['name']
        labels = {
            'name': 'Имя',
            'surname': 'Фамилия',
            'feedback': 'Отзыв',
            'rating': 'Рейтинг',
        }
        error_messages = {
                 'name': {
                     'max_length': 'Слишком много симваолов',
                     'min_length': 'Слишком мало симваолов',
                     'required': 'Хотя бы 1 символ',
                 },
                'surname': {
                    'max_length': 'Слишком много симваолов',
                    'min_length': 'Слишком мало симваолов',
                    'required': 'Хотя бы 1 символ',
                },
             }

















