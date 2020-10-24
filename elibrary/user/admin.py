from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import ugettext_lazy as _
from .models import User
# Register your models here.


class UserAdmin(BaseUserAdmin):
    ordering = ['email']
    list_display = ['email', 'firstname', 'lastname']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('lastname', 'firstname')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        (_('Last Login'), {'fields': ('last_login', )})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('email', 'lastname', 'firstname', 'password1', 'password2')
        }),
    )


admin.site.register(User, UserAdmin)
