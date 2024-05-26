from django.shortcuts import render, redirect, get_object_or_404
from .serializers import EmployeeSerializer, SkillSerializer
from .models import Employee, Skill
from rest_framework.viewsets import ModelViewSet
from .forms import EmployeeForms, SkillForm
import requests
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response

class SkillViewSet(ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

def employee_view(request):
    employee_form = EmployeeForms()
    skill_form = SkillForm()
    if request.method == 'POST':
        employee_form= EmployeeForms(data=request.POST)
        skill_form = SkillForm(data=request.POST)
        if employee_form.is_valid() and skill_form.is_valid():
            skill_name = request.POST.get('name')
            skill_names = skill_name.split(',')
            employee=employee_form.save(commit=False)
            employee.save()
            for skill in skill_names:
                skill_name=skill.strip()
                try:
                    existing_skill = Skill.objects.get(name=skill_name)
                    employee.skills.add(existing_skill)
                except Skill.DoesNotExist:
                    new_skill = Skill.objects.create(name=skill_name)
                    employee.skills.add(new_skill)
            return redirect(reverse('welcome'))
    return render(request, 'employee-form.html',{'employee_form':employee_form, 'skill_form':skill_form})

def skill_suggestion(request, term):
    skill_matched = Skill.objects.filter(name__icontains=term)
    skills_list = list(skill_matched.values('name'))
    return JsonResponse(skills_list, safe=False)

def welcome_view(request):
    url_emp = request.build_absolute_uri(reverse('employees-list'))
    response = requests.get(url_emp)
    employees=response.json() if response.status_code==200 else ''
    return render(request, 'success.html',{'employee_data':employees})

def emp_update(request,id):
    data=get_object_or_404(Employee, id=id)
    employee_form = EmployeeForms(instance=data)
    skills=', '.join([skill.name for skill in data.skills.all()])
    skill_form = SkillForm()
    skill_form.fields['name'].initial=skills
    if request.method=='POST':
        employee_form = EmployeeForms(request.POST, instance=data)
        skill_form = SkillForm(request.POST)
        if employee_form.is_valid() and skill_form.is_valid():
            obj, created = Employee.objects.update_or_create(
                first_name=employee_form.cleaned_data.get('first_name'),
                last_name =employee_form.cleaned_data.get('last_name'),
                email_id=employee_form.cleaned_data.get('email_id'),  
            )
            cleaned_skill = skill_form.cleaned_data.get('name')
            skill_names = [name.strip() for name in cleaned_skill.split(',') if name.strip()]
            for skill in skill_names:
                skill_name=skill.strip()
                try:
                    existing_skill = Skill.objects.get(name=skill_name) 
                    data.skills.add(existing_skill)
                except Skill.DoesNotExist:
                    new_skill = Skill.objects.create(name=skill_name)
                    data.skills.add(new_skill)
            return redirect(reverse('welcome'))
    return render(request,'employee-form.html',{'employee_form':employee_form,'skill_form':skill_form})

def emp_delete(request, id):
    employee=Employee.objects.get(id=id)
    employee.delete()
    url_emp = request.build_absolute_uri(reverse('employees-list'))
    response = requests.get(url_emp)
    employees=response.json() if response.status_code==200 else ''
    return render(request,'success.html',{'employee_data':employees})






    



