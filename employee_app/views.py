from rest_framework import viewsets, filters
from rest_framework.decorators import action,permission_classes
from rest_framework.response import Response
from django.http import HttpResponse
import csv
from .models import Employee, Attendance, Performance, Department
from .serializers import EmployeeSerializer, AttendanceSerializer, PerformanceSerializer, DepartmentSerializer
from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.shortcuts import render
from datetime import datetime
from datetime import timedelta
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


def home_view(request):
    return HttpResponse("Welcome to the Employee Management API")


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def health_check(request):
    return Response({"status": "ok"}, status=status.HTTP_200_OK)



@permission_classes([IsAuthenticated])
class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['first_name','last_name','email']
    ordering_fields = ['date_joined']

    @action(detail=False)
    def export_csv(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="employees.csv"'
        writer = csv.writer(response)
        writer.writerow(['ID','First name','Last name','Email','Department','Date joined'])
        for emp in self.get_queryset():
            writer.writerow([emp.id, emp.first_name, emp.last_name, emp.email, emp.department.name if emp.department else '', emp.date_joined])
        return response

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

class PerformanceViewSet(viewsets.ModelViewSet):
    queryset = Performance.objects.all()
    serializer_class = PerformanceSerializer



def performance_chart(request):
    # Get performance data for the last 30 days
    performance_data = Performance.objects.filter(review_date__gte=datetime.now() - timedelta(days=30))
    
    # Prepare data for chart
    employee_names = [emp.employee.first_name + " " + emp.employee.last_name for emp in performance_data]
    performance_scores = [emp.score for emp in performance_data]
    
    # Pass the data to the template
    context = {
        'employee_names': employee_names,
        'performance_scores': performance_scores
    }
    
    return render(request, 'employee_app/performance_chart.html', context)