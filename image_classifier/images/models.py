from django.db import models

class ImageDirectory(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()
    status = models.CharField(max_length=255, blank=True, null=True)  # To store training status
    results = models.JSONField(blank=True, null=True)  # To store results in JSON format

    def __str__(self):
        return self.name
