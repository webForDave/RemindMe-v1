from django.db import models

class Reminder(models.Model):

    NOTIFICATION_CHOICES = [
        ('email', 'Email'),
        ('sms', 'SMS'),
        ('both', "Email & SMS")
    ]

    title = models.CharField(max_length=30)
    description = models.TextField()
    reminder_time = models.DateTimeField()
    notification_type = models.CharField(max_length=20, choices=NOTIFICATION_CHOICES, default="email")
    contact = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title