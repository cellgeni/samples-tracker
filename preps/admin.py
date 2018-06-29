from django.contrib import admin
from .models import Stage, Action, Sample
# Register your models here.
admin.site.register(Sample)
admin.site.register(Stage)
admin.site.register(Action)