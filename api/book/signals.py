from django.contrib.auth.models import  Permission
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

User = get_user_model()


@receiver(post_save, sender=User)
def assign_permissions(sender, instance, created, **kwargs):
    if created:
        if  instance.groups.filter(name='Authors').exists():
            instance.user_permissions.add(Permission.objects.get(codename='can_crud_book'))
            instance.user_permissions.add(Permission.objects.get(codename='can_crud_page'))
        elif instance.groups.filter(name='Readers').exists():
            instance.user_permissions.add(Permission.objects.get(codename='can_read_book'))
            instance.user_permissions.add(Permission.objects.get(codename='can_read_page'))