from django.contrib import admin

# Register your models here.
from project.models import Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('proj_id', 'name', 'entry_url', 'created_at')


admin.site.register(Project, ProjectAdmin)
