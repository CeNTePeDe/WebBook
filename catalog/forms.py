from django import forms
from datetime import date
from django.forms import ModelForm
from .models import Book
from captcha.fields import CaptchaField


class AuthorForm(forms.Form):
    first_name = forms.CharField(label='Имя автора')
    last_name = forms.CharField(label='Фамилия автора')
    date_of_birth = forms.DateField(label='Дата рождения',
                                    initial=format(date.today()),
                                    widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    date_of_death = forms.DateField(label='Дата смерти',
                                    initial=format(date.today()),

                                    widget=forms.widgets.DateInput(attrs={'type': 'date'}))


class BookModelForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'genre', 'language', 'author', 'summary', 'isbn']
        labels = {'summary': ('Аннотация'), }
        help_text = {'summary': ('Не более 1000 символов'), }


class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=255)
    email = forms.EmailField(label='Email')
    content = forms.CharField(label='Контент', widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    captcha = CaptchaField()

