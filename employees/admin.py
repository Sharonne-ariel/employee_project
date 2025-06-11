from django.contrib import admin
from .models import Employee, Department, Performance

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'department', 'date_of_joining')
    list_filter = ('department', 'date_of_joining')
    search_fields = ('name', 'email', 'phone_number')

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Performance)
class PerformanceAdmin(admin.ModelAdmin):
    list_display = ('employee', 'rating', 'review_date')
    list_filter = ('rating', 'review_date')
    search_fields = ('employee__name',)
