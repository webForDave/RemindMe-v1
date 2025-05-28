from django.shortcuts import render
from .models import Reminder
from .serializers import ReminderSerializer
from rest_framework import viewsets

class ReminderViewset(viewsets.ModelViewSet):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer