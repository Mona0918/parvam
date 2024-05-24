from django.contrib import admin
from .models import Employee, Skill

class EmployeeAdmin(admin.ModelAdmin):
    autocomplete_fields = ['skills']

class SkillAdmin(admin.ModelAdmin):
    search_fields = ['name']
    def get_search_results(self, request, queryset, search_term):
        results = super().get_search_results(request, queryset, search_term)
        return results

admin.site.register(Employee)
admin.site.register(Skill)

