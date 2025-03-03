from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # Note: Removed avatar field from fieldsets and add_fieldsets to avoid conflict with django-avatar
    fieldsets = UserAdmin.fieldsets + (
        ('Custom fields', {'fields': ('bio', 'birth_date', 'phone', 'address', 'role')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('bio', 'birth_date', 'phone', 'address', 'role')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
