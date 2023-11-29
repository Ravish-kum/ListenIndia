# forms.py
from django import forms
from .models import ListenIN

class IndiaModelForm(forms.ModelForm):
    class Meta:
        model = ListenIN
        fields = ['title','video_file','language']
        
