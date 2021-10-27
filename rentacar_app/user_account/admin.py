from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account, ClientProfile


class AccountAdmin(UserAdmin):
    ordering = ('email',)
    list_display = ('email', 'first_name', 'last_name', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name', 'last_login')
    readonly_fields = ('id', 'date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'date_joined', 'last_login')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_admin', 'is_superuser')}),
        )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name',
                       'is_active', 'is_staff', 'is_admin', 'is_superuser'),
        }),

    )


class ClientProfileAdmin(UserAdmin):
    ordering = ('user',)
    list_display = ('user', 'phone_number', 'address1', 'address2', 'postcode', 'state', 'country', 'state_region')
    search_fields = ('user', 'phone_number', 'address1', 'address2', 'postcode', 'state', 'country', 'state_region')

    filter_horizontal = ()
    list_filter = ()


    fieldsets = (
        (None, {'fields': ('user',)}),
        ('Personal info', {'fields': ('phone_number', 'address1', 'address2', 'postcode', 'state', 'country', 'state_region')}),
        )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('user', 'phone_number', 'address1', 'address2', 'postcode', 'state', 'country', 'state_region'),
        }),

    )



admin.site.register(Account, AccountAdmin)
admin.site.register(ClientProfile, ClientProfileAdmin)





