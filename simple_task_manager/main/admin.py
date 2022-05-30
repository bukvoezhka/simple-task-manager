from django.contrib import admin
from simple_task_manager.main.models import ArchiveReport, Event, Category


class EventAdmin(admin.ModelAdmin):
    list_display = ('description', 'category', 'created_at', 'updated_at', 'archive_report')
    list_display_links = ('description',)
    list_editable = ('category', 'archive_report',)


admin.site.register(Event, EventAdmin)
admin.site.register(Category)
admin.site.register(ArchiveReport)
