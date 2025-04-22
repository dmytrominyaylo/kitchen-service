from django import forms
from .models import Dish, Cook
from django.contrib.auth.forms import UserCreationForm


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = [
            "name",
            "description",
            "price",
            "dish_type",
            "cooks",
            "ingredients"
        ]
        widgets = {
            "description": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Describe the dish..."
                }
            ),
            "cooks": forms.SelectMultiple(attrs={"class": "form-control"}),
            "ingredients": forms.CheckboxSelectMultiple(),
        }
        help_texts = {
            "price": "Enter the price in UAH (no fractional values)",
            "ingredients": "Select all ingredients included in the dish",
        }


class CookCreationForm(UserCreationForm):
    class Meta:
        model = Cook
        fields = (
            "username",
            "first_name",
            "last_name",
            "years_of_experience",
            "password1",
            "password2"
        )


class CookUpdateForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = ("first_name", "last_name", "years_of_experience")
        widgets = {
            "years_of_experience": forms.NumberInput(
                attrs={
                    "min": 0,
                    "max": 100
                }
            ),
        }

    def clean_years_of_experience(self):
        value = self.cleaned_data["years_of_experience"]
        if value > 100:
            raise forms.ValidationError("Too many years of experience!")
        return value
