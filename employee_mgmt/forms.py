from django import forms
from .models import Employee, Skill
from django.core.exceptions import ValidationError

class EmployeeForms(forms.ModelForm):
    class Meta:
        model=Employee
        fields=['first_name','last_name','email_id']
        labels={
            'first_name':'First Name',
            'last_name':'Last Name',
            "email_id":'Email',
        }
        
    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if not first_name.isalpha():
            raise ValidationError("Only Alphabets can be accepted")
        else:
            return first_name
        
    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if not last_name.isalpha():
            raise ValidationError("Only Alphabets can be accepted")
        else:
            return last_name
    
class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['name']
        labels = {
            'name':'Skills',
        }
        widgets = {
            'name': forms.TextInput(attrs={'autocomplete':'off'})
        }



