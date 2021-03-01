from .models import Student
from django import forms

class StudentForm(forms.Form):
    name = forms.IntegerField()
    studentClass = forms.CharField(max_length=255)





