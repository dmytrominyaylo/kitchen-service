from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Dish, DishType, Cook


@admin.register(Cook)
class CookAdmin(UserAdmin):
    model = Cook
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("years_of_experience",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("years_of_experience",)}),
    )


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "dish_type")
    list_filter = ("dish_type",)
    search_fields = ("name", "description")


admin.site.register(DishType)
