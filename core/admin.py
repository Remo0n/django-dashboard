from django.contrib import admin
from django.contrib.auth.models import User, Group

from core.models import Device, Ratification
from rangefilter.filters import DateRangeFilter


class DeviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'entry_date', 'delivery_entity', 'delivery_engineer', 'type', 'serial_number', '_is_custody'
                    , 'receiver_engineer', 'fixing_engineer', 'action', 'maintenance_date', 'maintenance_state'
                    , 'receiver_name', 'sender_name', 'sending_date', 'register_date', 'ratification_doc'
                    , 'ratification_date', 'register_number', 'exiting_date_1', 'responsible_person_1', 'exiting_date_2'
                    , 'responsible_person_2', 'exiting_date_3', 'responsible_person_3', 'exiting_date_4'
                    , 'responsible_person_4')
    search_fields = ('serial_number',)
    list_filter = ('_is_custody', 'delivery_entity', ('entry_date', DateRangeFilter),)
    fieldsets = (
        ('بيانات الدخول', {
            'fields': (
                'entry_date', 'serial_number', 'type', 'receiver_engineer', 'delivery_engineer', 'delivery_entity',
                'fixing_engineer', 'action',),
            'classes': ('order-0', 'baton-tabs-init', 'baton-tab-fs-register', 'baton-tab-fs-deliver'
                        , 'baton-tab-fs-custody',),
            'description': 'This is a description text'

        }),
        ('تسجيل الحالة الفنية', {
            'fields': ('maintenance_date', 'maintenance_state',),
            'classes': ('tab-fs-register',),
            'description': 'This is another description text'

        }),
        ('بيانات التسليم', {
            'fields': ('receiver_name', 'sender_name', 'sending_date'),
            'classes': ('tab-fs-deliver',),
            'description': 'This is another description text'
        }),
        ('فى حالة العهدة', {
            'fields': ('register_date', 'register_person', 'ratification_doc', 'ratification_date', 'register_number'
                       , 'exiting_date_1', 'responsible_person_1', 'exiting_date_2', 'responsible_person_2'
                       , 'exiting_date_3', 'responsible_person_3', 'exiting_date_4', 'responsible_person_4'),
            'classes': ('tab-fs-custody',),
            'description': 'This is another description text'
        }),
    )


# Register your models here.
admin.site.register(Device, DeviceAdmin)
admin.site.register(Ratification)

# Unregister Device Model
admin.site.unregister(User)
admin.site.unregister(Group)
