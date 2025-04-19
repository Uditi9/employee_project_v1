from rest_framework import serializers
from .models import Employee, Department, Attendance, Performance

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name']

class EmployeeSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()

    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'email', 'department', 'date_joined']

class AttendanceSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer()

    class Meta:
        model = Attendance
        fields = ['id', 'employee', 'date', 'status']

class PerformanceSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer()

    class Meta:
        model = Performance
        fields = ['id', 'employee', 'score', 'review_date', 'comments']
