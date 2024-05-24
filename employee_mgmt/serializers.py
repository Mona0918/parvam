from rest_framework import serializers
from .models import Employee, Skill
from dal import autocomplete
from django.urls import reverse

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    skills=SkillSerializer(many=True)
    class Meta:
        model = Employee
        fields=['id','first_name','last_name','email_id','skills']

    def __init__(self, *args, **kwargs):
        super(EmployeeSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and request.method in ['POST','PUT']:
            self.fields['skills']=serializers.PrimaryKeyRelatedField(many=True, queryset=Skill.objects.all())

    







        

