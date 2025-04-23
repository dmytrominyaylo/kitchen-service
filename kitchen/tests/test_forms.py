from django.test import TestCase
from kitchen.forms import CookCreationForm, DishForm
from kitchen.models import DishType, Ingredient, Cook


class CookFormTests(TestCase):
    def test_create_cook_form_valid(self):
        form_data = {
            "username": "newchef",
            "first_name": "Alice",
            "last_name": "Smith",
            "years_of_experience": 7,
            "password1": "S3cur3TestP@ssw0rd!",
            "password2": "S3cur3TestP@ssw0rd!"
        }
        form = CookCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_create_cook_form_invalid(self):
        form_data = {
            "username": "newchef",
            "first_name": "Alice",
            "last_name": "Smith",
            "years_of_experience": 7,
            "password1": "S3cur3TestP@ssw0rd!",
            "password2": "wrongpassword"
        }
        form = CookCreationForm(data=form_data)
        self.assertFalse(form.is_valid())


class DishFormTests(TestCase):
    def setUp(self):
        self.dish_type = DishType.objects.create(name="Soup")
        self.ingredient1 = Ingredient.objects.create(name="Tomato")
        self.ingredient2 = Ingredient.objects.create(name="Salt")
        self.cook1 = Cook.objects.create_user(
            username="cook1", password="C00kP@ssword"
        )

    def test_dish_form_valid(self):
        form_data = {
            "name": "Tomato Soup",
            "description": "Delicious homemade soup",
            "price": "59.99",
            "dish_type": self.dish_type.id,
            "cooks": [self.cook1.id],
            "ingredients": [self.ingredient1.id, self.ingredient2.id]
        }
        form = DishForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_dish_form_invalid(self):
        form_data = {
            "name": "",
            "description": "Missing name",
            "price": "0.00",
            "dish_type": "",
            "cooks": [],
            "ingredients": []
        }
        form = DishForm(data=form_data)
        self.assertFalse(form.is_valid())
