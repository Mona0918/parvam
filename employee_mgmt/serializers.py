from rest_framework import serializers
from .models import Employee, Skill
from dal import autocomplete
from django.urls import reverse

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    skills=SkillSerializer(many=True, required=False)
    class Meta:
        model = Employee
        fields=['id','first_name','last_name','email_id','skills']


    







        

