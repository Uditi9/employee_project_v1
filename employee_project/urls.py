from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from employee_app.views import performance_chart

# Swagger view setup
schema_view = get_schema_view(
    openapi.Info(title="Employee API", default_version='v1'),
    public=True, permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('performance-chart/', performance_chart, name='performance_chart'),  
    # Point the root URL to Swagger UI
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # Root to Swagger
    path('admin/', admin.site.urls),
    path('api/', include('employee_app.urls')),  # Employee app URLs for API
    path('health/', lambda request: JsonResponse({'status': 'ok'})),
]
