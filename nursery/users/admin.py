from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from .models import (UserData, PlantDetails, OrderDetails)


class MyUserAdmin(UserAdmin):
    model = UserData
    list_display = ('email', 'first_name', 'last_login',
                    'is_admin', 'is_staff')
    search_fields = ('email', 'first_name',)
    readonly_fields = ('last_login',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(UserData, MyUserAdmin)

admin.site.register(PlantDetails)
admin.site.register(OrderDetails)
