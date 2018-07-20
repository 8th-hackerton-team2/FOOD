from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from members.models import User


class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': (
            'username',
            'password')}),
        ('개인정보', {'fields': (
            'last_name',
            'first_name',
            'email',
            'img_profile',)}),
        ('권한', {'fields': (
            'is_active',
            'is_staff',
            'is_superuser',)}),
        ('주요일자', {'fields': (
            'last_login',
            'date_joined')}),
    )


admin.site.register(User, UserAdmin)