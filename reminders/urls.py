from rest_framework.routers import DefaultRouter
from .views import ReminderViewset
from django.urls import path, include

router = DefaultRouter()
router.register(r"reminders", ReminderViewset, basename="reminder")

urlpatterns = [
    path("", include(router.urls)),
]