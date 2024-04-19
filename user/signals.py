from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import (User, WarehouseCommonProfile, GatehouseProfile, ReceptionistProfile,
                     WarehouseOperativeProfile, WarehouseAdminProfile, WarehouseTeamLeaderProfile,
                     WarehouseManagerProfile, InventoryAdminProfile, InventoryTeamLeaderProfile,
                     InventoryManagerProfile, OperationalManagerProfile)

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role == User.Role.WAREHOUSE_COMMON:
            WarehouseCommonProfile.objects.create(user=instance)
        elif instance.role == User.Role.GATEHOUSE:
            GatehouseProfile.objects.create(user=instance)
        elif instance.role == User.Role.RECEPTIONIST:
            ReceptionistProfile.objects.create(user=instance)
        elif instance.role == User.Role.WAREHOUSE_OPERATIVE:
            WarehouseOperativeProfile.objects.create(user=instance)
        elif instance.role == User.Role.WAREHOUSE_ADMIN:
            WarehouseAdminProfile.objects.create(user=instance)
        elif instance.role == User.Role.WAREHOUSE_TEAM_LEADER:
            WarehouseTeamLeaderProfile.objects.create(user=instance)
        elif instance.role == User.Role.WAREHOUSE_MANAGER:
            WarehouseManagerProfile.objects.create(user=instance)
        elif instance.role == User.Role.INVENTORY_ADMIN:
            InventoryAdminProfile.objects.create(user=instance)
        elif instance.role == User.Role.INVENTORY_TEAM_LEADER:
            InventoryTeamLeaderProfile.objects.create(user=instance)
        elif instance.role == User.Role.INVENTORY_MANAGER:
            InventoryManagerProfile.objects.create(user=instance)
        elif instance.role == User.Role.OPERATIONAL_MANAGER:
            OperationalManagerProfile.objects.create(user=instance)
    else:
        if hasattr(instance, 'profile'):
            instance.profile.save()  
            
    
