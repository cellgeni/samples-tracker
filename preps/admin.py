from django.contrib import admin
from .models import Stage, Action, Sample, Owner, Project


class ProjectAdmin(admin.ModelAdmin):
    list_display = ["cost_code", "balance_avail", "is_core"]
    ordering = ('balance_avail', "is_core", "cost_code")

admin.site.register(Sample)
admin.site.register(Stage)
admin.site.register(Action)
admin.site.register(Owner)
admin.site.register(Project, ProjectAdmin)
