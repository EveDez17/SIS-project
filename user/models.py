from django.db import models

class Department(models.Model):
    department_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.department_name

class Role(models.Model):
    role_title = models.CharField(max_length=100)
    role_description = models.TextField()
    
    def __str__(self):
        return self.title

class Employee(models.Model):
    employee_first_name = models.CharField(max_length=100)
    employee_last_name = models.CharField(max_length=100)
    employee_street_number = models.CharField(max_length=128)
    employee_street_name = models.CharField(max_length=255)
    employee_city = models.CharField(max_length=255)
    employee_county = models.CharField(max_length=255)
    employee_country = models.CharField(max_length=255)
    employee_post_code = models.CharField(max_length=20, unique=True)
    date_hired = models.DateField()
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True, related_name='employees')
    
    def __str__(self):
        return f"{self.employee_first_name} {self.employee_last_name}"
    
class EmployeeRole(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    assigned_date = models.DateField()  

    