from django.shortcuts import render
from .serializers import EmployeeSerializer, SkillSerializer
from .models import Employee, Skill
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from dal import autocomplete

class SkillViewSet(ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


    



