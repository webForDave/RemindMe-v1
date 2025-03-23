from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        fields = UserCreationForm.Meta.fields + ("name",)
        model = CustomUser

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        fields = UserChangeForm.Meta.fields
        model = CustomUser