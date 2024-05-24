from django.shortcuts import render
from .serializers import EmployeeSerializer, SkillSerializer
from .models import Employee, Skill
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from dal import autocomplete

class SkillViewSet(ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['skills__name']

class SkillAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Skill.objects.all()

        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs

    



