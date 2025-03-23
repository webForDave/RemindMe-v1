from django.contrib import admin
from .models import Reminder

class ReminderAdmin(admin.ModelAdmin):
    readonly_fields = ["contact_details"]
    list_display = ["title", "description", "date", "contact_details" ]

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.contact_details = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Reminder, ReminderAdmin)