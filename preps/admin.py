from django.contrib import admin
from .models import Stage, Action, Sample, Owner

admin.site.register(Sample)
admin.site.register(Stage)
admin.site.register(Action)
admin.site.register(Owner)
