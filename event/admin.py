from django.contrib import admin

from .models import Event, EventRegistration


# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'max_attendees', 'num_of_registered', 'category', 'status')
    list_filter = ('status', 'category',)
    fieldsets = (
        (None, {
            'fields': ('title', 'organizer', 'description', 'start_date', 'end_date')
        }),
        (None, {
            'fields': ('num_of_registered', 'max_attendees', 'category', 'status')
        }),
        ('Location', {
            'fields': ('address_line1', 'address_line2', 'zipCode', 'city', 'country')
        })

    )

    # def save_model(self, request, obj, form, change):
    #     obj.organizer = request.user
    #     obj.save()


class EventRegistrationAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'registration_date')

    def title(self, obj):
        return obj.event.title

    def user(self, obj):
        return obj.user.email


admin.site.register(Event, EventAdmin)
admin.site.register(EventRegistration, EventRegistrationAdmin)

# Todo Give admin ability to select the organizer but only via admin panel
