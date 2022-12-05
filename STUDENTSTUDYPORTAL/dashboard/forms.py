from django import forms
from .models import *
from django.forms import widgets
from django.contrib.auth.forms import UserCreationForm


# ------------  Notes Section  ------------------#

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['title', 'description']


# -------- Homework Section ------------#

class DateInput(forms.DateInput):
    input_type = 'date'


class HomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        widgets = {'due': DateInput()}
        fields = ['subject', 'title', 'description', 'due', 'is_finished']


# -------- Common Section ------------ #

class DashboardForm(forms.Form):
    text = forms.CharField(max_length=100, label="Enter Youtube Search :")


# -------- To Do Section ------------ #

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'is_finished']


# -------- Conversion Section ------------ #

class ConversionForm(forms.Form):
    CHOICES = [('length', 'Length'), ('mass', 'Mass')]
    measurement = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)


class ConversionalLengthForm(forms.Form):
    CHOICES = [('yard', 'Yard'), ('foot', 'Foot')]
    input = forms.ChoiceField(required=False, label=False, widget=forms.TextInput(
        attrs={'type': 'number', 'placeholder': 'Enter the Number'}
    ))
    measure1 = forms.CharField(
        label='', widget=forms.Select(choices=CHOICES)
    )
    measure2 = forms.CharField(
        label='', widget=forms.Select(choices=CHOICES)
    )


class ConversionalMassForm(forms.Form):
    CHOICES = [('pound', 'Pound'), ('kilogram', 'Kilogram')]
    input = forms.ChoiceField(required=False, label=False, widget=forms.TextInput(
        attrs={'type': 'number', 'placeholder': 'Enter the Number'}
    ))
    measure1 = forms.CharField(
        label='', widget=forms.Select(choices=CHOICES)
    )
    measure2 = forms.CharField(
        label='', widget=forms.Select(choices=CHOICES)
    )


# -------- Login Section ------------ #

class UseRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
