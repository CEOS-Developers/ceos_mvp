from django.contrib import admin
from core.models import Email


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ('email', 'submitted_from', 'created_at')
