from django.test import TestCase
from django.contrib.auth import get_user_model
from kitchen.models import DishType, Dish, Ingredient

User = get_user_model()


class DishTypeModelTest(TestCase):
    def test_str_representation(self):
        dish_type = DishType.objects.create(name="Dessert")
        self.assertEqual(str(dish_type), "Dessert")


class IngredientModelTest(TestCase):
    def test_str_representation(self):
        ingredient = Ingredient.objects.create(name="Sugar")
        self.assertEqual(str(ingredient), "Sugar")


class CookModelTest(TestCase):
    def test_str_representation(self):
        cook = User.objects.create_user(
            username="chefjohn",
            password="test1234",
            first_name="John",
            last_name="Doe"
        )
        self.assertEqual(str(cook), "chefjohn (John Doe)")

    def test_default_experience(self):
        cook = User.objects.create_user(
            username="chefjane",
            password="test1234"
        )
        self.assertEqual(cook.years_of_experience, 0)


class DishModelTest(TestCase):
    def setUp(self):
        self.dish_type = DishType.objects.create(name="Main")
        self.cook = User.objects.create_user(username="chef", password="pass")
        self.ingredient = Ingredient.objects.create(name="Tomato")

    def test_str_representation(self):
        dish = Dish.objects.create(
            name="Pasta",
            description="Delicious Italian pasta",
            price=10.50,
            dish_type=self.dish_type
        )
        dish.cooks.add(self.cook)
        dish.ingredients.add(self.ingredient)

        self.assertEqual(str(dish), "Pasta")
