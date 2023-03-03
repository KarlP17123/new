from django.contrib import admin
from .models import UserProfile
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from . models import User
from django.contrib.auth import get_user_model

# Register your models here.
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )



admin.site.register(get_user_model(), UserAdmin)
admin.site.register(UserProfile)

