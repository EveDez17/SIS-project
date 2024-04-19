from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.apps import apps
from django.utils.translation import gettext_lazy as _

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
    

class User(AbstractUser):
    
    class Role(models.TextChoices):
        WAREHOUSE_COMMON = "WAREHOUSE_COMMON", _('Warehouse common')
        GATEHOUSE = "GATEHOUSE", _('Gatehouse')
        RECEPTIONIST = "RECEPTIONIST", _('Receptionist')
        WAREHOUSE_OPERATIVE = "WAREHOUSE_OPERATIVE", _('Warehouse Operative')
        WAREHOUSE_ADMIN = "WAREHOUSE_ADMIN", _('Warehouse Admin')
        WAREHOUSE_TEAM_LEADER = "WAREHOUSE_TEAM_LEADER", _('Warehouse Team Leader')
        WAREHOUSE_MANAGER = "WAREHOUSE_MANAGER", _('Warehouse Manager')
        INVENTORY_ADMIN = "INVENTORY_ADMIN", _('Inventory Admin')
        INVENTORY_TEAM_LEADER = "INVENTORY_TEAM_LEADER", _('Inventory Team Leader')
        INVENTORY_MANAGER = "INVENTORY_MANAGER", _('Inventory Manager')
        OPERATIONAL_MANAGER = "OPERATIONAL_MANAGER", _('Operational Manager')

    role = models.CharField(_('Role'), max_length=100, choices=Role.choices, default=Role.WAREHOUSE_COMMON)
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True, verbose_name=_("Department"))
    phone_number = models.CharField(_("Phone Number"), max_length=15, blank=True, null=True)
    
    def get_absolute_url(self):
        return reverse("user:detail", kwargs={"username": self.username})

    def __str__(self):
        return f"{self.name} ({self.get_role_display()})"

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

# Custom related_name definitions
User._meta.get_field('groups').remote_field.related_name = 'custom_user_groups'
User._meta.get_field('user_permissions').remote_field.related_name = 'custom_user_user_permissions'

class WarehouseCommonProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='warehouse_common_profile')
    department = models.TextField()

class GatehouseProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='gatehouse_profile')
    access_level = models.CharField(max_length=100)

class ReceptionistProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='receptionist_profile')
    shift_hours = models.CharField(max_length=100)
    
class WarehouseOperativeProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='receptionist_profile')
    shift_hours = models.CharField(max_length=100)
    
class WarehouseAdminProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='receptionist_profile')
    shift_hours = models.CharField(max_length=100)
    
class WarehouseTeamLeaderProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='receptionist_profile')
    shift_hours = models.CharField(max_length=100)
    
class WarehouseManagerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='receptionist_profile')
    shift_hours = models.CharField(max_length=100)
    
class InventoryAdminProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='receptionist_profile')
    shift_hours = models.CharField(max_length=100)
    
class InventoryTeamLeaderProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='receptionist_profile')
    shift_hours = models.CharField(max_length=100)
    
class InventoryManageProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='receptionist_profile')
    shift_hours = models.CharField(max_length=100)
    
class OperationalManagerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='receptionist_profile')
    shift_hours = models.CharField(max_length=100)


