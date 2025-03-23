from django.db import models
from django.conf import settings

class Reminder(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField(default=None, blank=True)
    contact_details = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title