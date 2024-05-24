from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router=DefaultRouter()
router.register(r'skill', views.SkillViewSet, basename='skill')
router.register(r'employees', views.EmployeeViewSet, basename='employees')

urlpatterns = [
    path('api/', include(router.urls)),
    path('skill-autocomplete/', views.SkillAutocomplete.as_view(create_field='name', validate_create=True), name='skill-autocomplete'),
]