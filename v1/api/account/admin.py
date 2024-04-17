from .models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserModelAdmin(BaseUserAdmin):
    list_display = ['id', 'email', 'user_name', 'is_admin']
    list_filter = ['is_admin',]
    fieldsets = [
        ['User Credentials', {'fields': ['email', 'password']}],
        ['Personal Info', {'fields': ['user_name', 'is_blocked']}],
        ['Permisions', {'fields': ['is_admin',
                                   'is_staff', 'is_superuser', 'is_active']}],
    ]
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'password', 'password2')
        })
    )
    search_fields = ('email', 'user_name')
    ordering = ('email', 'id')
    filter_horizontal = ()


admin.site.register(User, UserModelAdmin)
