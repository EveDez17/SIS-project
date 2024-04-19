from django.contrib import admin
from .models import Department, Employee, Role, EmployeeRole

admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Role)
admin.site.register(EmployeeRole)
