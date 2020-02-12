from django.contrib import admin

from .models import * #Species, Feature

# Register your models here.
admin.site.register(Species)
admin.site.register(Feature)
