from django.contrib import admin
from core.models import Email, Site


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ('email', 'submitted_from', 'created_at')


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url', 'vote_count')
