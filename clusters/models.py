from django.db import models
from tools.tools import file_handler


# Cluster Model
class Cluster(models.Model):
    name = models.CharField(null=False, blank=False, unique=True, max_length=100)
    host = models.URLField(null=False, blank=False, unique=True)
    ssl = models.BooleanField(default=False)
    config_file = models.FileField(blank=True, null=True, upload_to=file_handler)

    def __str__(self):
        return self.name
