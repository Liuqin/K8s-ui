from django.contrib import admin
from .models import *


class ClusterAdmin(admin.ModelAdmin):
    pass


class ResourceAdmin(admin.ModelAdmin):
    pass


admin.site.register(Cluster, ClusterAdmin)
admin.site.register(Resource, ResourceAdmin)
