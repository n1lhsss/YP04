from django.contrib import admin  
from django.contrib.auth.admin import UserAdmin  # pyright: ignore[reportMissingImports]

from models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """Расширяем стандартнгую админку User.

    list_display - колонки в списке.
    list_filter - фильтры справа.
    fieldsets - секции в форме редактирования.
    """
    
    list_display = ("username", "full_name", "role", "is_active")
    list_filter = ("role", "is_active")
    fieldsets = UserAdmin.fieldsets + (
        ("Дополнительно", {"fields": ("full_name", "role")}),
    )

