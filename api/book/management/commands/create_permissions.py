# your_app/management/commands/create_permissions.py

from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType


class Command(BaseCommand):
    def handle(self, *args, **options):
        Author_group, _ = Group.objects.get_or_create(name='Authors')
        Readers_group, _ = Group.objects.get_or_create(name='Readers')
        content_type_book = ContentType.objects.get(app_label='book', model='book')
        content_type_page = ContentType.objects.get(app_label='book', model='pages')
        permission_read_only_book = Permission.objects.get(content_type=content_type_book, codename='view_book')
        permission_read_only_page = Permission.objects.get(content_type=content_type_page, codename='view_pages')
        Readers_group.permissions.add(permission_read_only_book)
        Readers_group.permissions.add(permission_read_only_page)

        permission_read_book = Permission.objects.get(content_type=content_type_book, codename='view_book')
        permission_read_page = Permission.objects.get(content_type=content_type_page, codename='view_pages')
        permission_create_book = Permission.objects.get(content_type=content_type_book, codename='add_book')
        permission_create_page = Permission.objects.get(content_type=content_type_page, codename='add_pages')
        permission_delete_book = Permission.objects.get(content_type=content_type_book, codename='delete_book')
        permission_delete_page = Permission.objects.get(content_type=content_type_page, codename='delete_pages')
        permission_update_book = Permission.objects.get(content_type=content_type_book, codename='change_book')
        permission_update_page = Permission.objects.get(content_type=content_type_page, codename='change_pages')

        Author_group.permissions.add(permission_read_book)
        Author_group.permissions.add(permission_read_page)
        Author_group.permissions.add(permission_create_book)
        Author_group.permissions.add(permission_create_page)
        Author_group.permissions.add(permission_delete_book)
        Author_group.permissions.add(permission_delete_page)
        Author_group.permissions.add(permission_update_book)
        Author_group.permissions.add(permission_update_page)
        self.stdout.write(self.style.SUCCESS('Permissions created successfully.'))
