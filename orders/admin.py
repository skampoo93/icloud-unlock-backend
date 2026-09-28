from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id", "user", "device_type", "serial_number",
        "status", "created_at",
    )
    list_filter = ("device_type", "status", "created_at")
    search_fields = ("serial_number", "user__username", "user__email")
    readonly_fields = ("user", "device_type", "serial_number", "created_at", "updated_at")
    list_editable = ("status",)
