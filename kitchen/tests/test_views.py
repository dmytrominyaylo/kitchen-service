from django.test import TestCase
from django.urls import reverse
from kitchen.models import Cook, Dish, DishType


class TestViews(TestCase):
    def setUp(self):
        self.user = Cook.objects.create_user(
            username="testuser",
            password="testpassword",
        )
        dish_type = DishType.objects.create(name="Main Course")
        self.dish = Dish.objects.create(
            name="Test Dish",
            description="Tasty",
            price=10.00,
            dish_type=dish_type
        )
        self.client.login(username="testuser", password="testpassword")

    def test_index_view(self):
        response = self.client.get(reverse("kitchen:index"))
        self.assertEqual(response.status_code, 200)

    def test_dish_list_view(self):
        response = self.client.get(reverse("kitchen:dish_list"))
        self.assertEqual(response.status_code, 200)

    def test_dish_detail_view(self):
        response = self.client.get(
            reverse(
                "kitchen:dish_detail",
                args=[self.dish.id]
            )
        )
        self.assertEqual(response.status_code, 200)

    def test_cook_list_view(self):
        response = self.client.get(reverse("kitchen:cook_list"))
        self.assertEqual(response.status_code, 200)

    def test_cook_create_view(self):
        form_data = {
            "username": "newcook",
            "password1": "StrongPass123",
            "password2": "StrongPass123",
        }
        response = self.client.post(reverse("kitchen:cook_create"), form_data)
        self.assertEqual(response.status_code, 200)

    def test_cook_delete_view(self):
        response = self.client.get(
            reverse(
                "kitchen:cook_delete",
                args=[self.user.id]
            )
        )
        self.assertEqual(response.status_code, 200)
