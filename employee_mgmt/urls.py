from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router=DefaultRouter()
router.register(r'skill', views.SkillViewSet, basename='skill')
router.register(r'employees', views.EmployeeViewSet, basename='employees')

urlpatterns = [
    path('api/', include(router.urls)),
    path('employee-form/', views.employee_view, name='employee-form'),
    path('skill_suggestion/<str:term>/', views.skill_suggestion, name='skill-suggestion'),
    path('welcome/', views.welcome_view, name="welcome"),
    path('employee-data-update/<int:id>/',views.emp_update, name="emp-update"),
    path('emp-delete/<int:id>/',views.emp_delete, name="emp-delete")
]