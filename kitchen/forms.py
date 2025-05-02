from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from kitchen.models import Dish, Cook, DishType


class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = (
            "name",
            "dish_type",
            "price",
        )


class CookCreationForm(UserCreationForm):
    class Meta:
        model = Cook
        fields = (
            "first_name",
            "last_name",
            "years_of_experience",
        )

    def clean_years_of_experience(self):
        return validate_years_of_experience(
            self.cleaned_data["years_of_experience"]
        )


class CookExperienceUpdateForm(forms.ModelForm):
    class Meta:
        model = Cook
        fields = ["years_of_experience"]

    def clean_years_of_experience(self):
        return validate_years_of_experience(
            self.cleaned_data["years_of_experience"]
        )


def validate_years_of_experience(years_of_experience):
    if not isinstance(years_of_experience, int):
        raise ValidationError("Years of experience must be a number.")

    if years_of_experience < 0 or years_of_experience > 50:
        raise ValidationError("Years of experience must be between 0 and 50.")

    return years_of_experience


class CookUsernameSearchForm(forms.Form):
    username = forms.CharField(
        required=False,
        max_length=255,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by username"
            }
        )
    )


class DishNameSearchForm(forms.Form):
    name = forms.CharField(
        required=False,
        max_length=255,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by name"
            }
        )
    )


class DishTypeNameSearchForm(forms.Form):
    name = forms.CharField(
        required=False,
        max_length=255,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by name"
            }
        )
    )
