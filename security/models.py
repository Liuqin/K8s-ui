from django.db import models
from django.contrib.auth.models import User


# User Profile Model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cluster = models.ManyToManyField('clusters.Cluster', related_name='clusters')
    resource = models.ManyToManyField('resources.Resource', related_name='modules')

    def __str__(self):
        return self.user
