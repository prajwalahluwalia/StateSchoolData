from django import forms
from basic_app.models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','age']