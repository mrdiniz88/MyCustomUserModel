from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.db import models

from .forms import UserCreationForm, UserChangeForm
from .models import User

@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    form =UserChangeForm
    add_form = UserCreationForm
    models = User
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        ("Campos personalizados", {"fields": ("bio",)}),
    )