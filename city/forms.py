from django import forms
from .models import Team, Applicant


from django.forms import ModelForm
  
class EntryForm(ModelForm):
  
    class Meta:
        model = Applicant
        fields = ['competition','city']