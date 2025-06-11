# employees/urls.py

from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, DepartmentViewSet, AttendanceViewSet, PerformanceViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'attendance', AttendanceViewSet)
router.register(r'performance', PerformanceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
