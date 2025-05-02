from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.urls import reverse


class DishType(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]
        verbose_name = "Dish Type"
        verbose_name_plural = "Dish Types"

    def __str__(self):
        return self.name


class Cook(AbstractUser):
    years_of_experience = models.PositiveIntegerField(default=0)

    groups = models.ManyToManyField(
        Group,
        related_name="cook_set",
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="cook_set_permissions",
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

    class Meta:
        ordering = ["username"]
        verbose_name = "Cook"
        verbose_name_plural = "Cooks"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE)
    cooks = models.ManyToManyField(Cook, related_name="dishes")

    class Meta:
        ordering = ["name"]
        verbose_name = "Dish"
        verbose_name_plural = "Dishes"

    def __str__(self):
        return self.name
