from django.db import models


class TrackingModel(models.Model):
    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ('-created',)
