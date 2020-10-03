from django.db import models


# Cluster Resource Model
class Resource(models.Model):
    name = models.CharField(blank=False, null=False, unique=True, max_length=80)
    slug = models.CharField(blank=False, null=False, unique=True, max_length=80)
    hasDelete = models.BooleanField(default=False)
    hasNamespace = models.BooleanField(default=False)
    sample = models.TextField(blank=False, null=False)

    def __str__(self):
        return self.name
