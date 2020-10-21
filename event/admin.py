from django.contrib import admin

from .models import Event, EventRegistration


# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'open_slots_left', 'category', 'status')
    list_filter = ('status', 'category',)
    readonly_fields = ('organizer',)
    fieldsets = (
        (None, {
            'fields': ('title', 'organizer', 'description', 'start_date', 'end_date')
        }),
        ('Location', {
            'fields': ('address_line1', 'address_line2', 'zipCode', 'city', 'country')
        }),
        (None, {
            'fields': ('open_slots_left', 'category', 'status')
        })
    )

    def save_model(self, request, obj, form, change):
        obj.organizer = request.user
        obj.save()


class EventRegistrationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user')

    def title(self, obj):
        return obj.event.title

    def user(self, obj):
        return obj.user.email


admin.site.register(Event, EventAdmin)
admin.site.register(EventRegistration, EventRegistrationAdmin)
