from django.contrib import admin

from resources.models import Resource, Location, Category

# Register your models here.
admin.site.register(Resource)
admin.site.register(Location)
admin.site.register(Category)