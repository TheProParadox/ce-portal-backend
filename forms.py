from django import forms
from .models import Entry


from django.forms import ModelForm
  
class EntryForm(ModelForm):
  
    class Meta:
        model = Entry
        fields = "__all__"