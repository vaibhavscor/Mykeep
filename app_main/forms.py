from django.forms import ModelForm
from .models import Note
from django import forms

class CreateNoteForm(forms.ModelForm):
	class Meta:
		model = Note
		widgets = {
            'Title': forms.TextInput(attrs={'class': 'myfieldclass'}),
        }
		fields = '__all__'