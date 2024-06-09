from django.contrib import admin
from.models import ScrapingJob, ScrapingTask

@admin.register(ScrapingJob)
class ScrapingJobAdmin(admin.ModelAdmin):
    list_display = ('job_id', 'tatus')
    list_filter = ('status',)
    search_fields = ('job_id',)

@admin.register(ScrapingTask)
class ScrapingTaskAdmin(admin.ModelAdmin):
    list_display = ('coin', 'output')
    list_filter = ('coin',)
    search_fields = ('coin',)

admin.site.site_header = 'Koina Skrapado Administrado'
admin.site.site_title = 'Koina Skrapado Administrado'
admin.site.index_title = 'Administrado de Koina Skrapado'