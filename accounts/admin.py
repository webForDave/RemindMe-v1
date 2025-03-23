from django.contrib import admin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["username", "email", "name", "is_staff"]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("name",)}),)
    add_fieldsets = ((None, {
        "classes": ("wide",),
        "fields": ("username", "email", "name", "password1", "password2",),
    }),)

admin.site.register(CustomUser, CustomUserAdmin)