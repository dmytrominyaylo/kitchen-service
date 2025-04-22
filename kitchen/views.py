from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Dish, Cook
from .forms import DishForm, CookCreationForm, CookUpdateForm


class DishListView(LoginRequiredMixin, generic.ListView):
    model = Dish
    context_object_name = "dishes"
    template_name = "dish_list.html"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class DishDetailView(LoginRequiredMixin, generic.DetailView):
    model = Dish
    context_object_name = "dish"
    template_name = "dish_detail.html"


class DishCreateView(LoginRequiredMixin, generic.CreateView):
    model = Dish
    form_class = DishForm
    template_name = "dish_form.html"
    success_url = reverse_lazy("dish_list")


class DishUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Dish
    form_class = DishForm
    template_name = "dish_form.html"
    success_url = reverse_lazy("dish_list")


class DishDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Dish
    template_name = "dish_confirm_delete.html"
    success_url = reverse_lazy("dish_list")


class CookListView(LoginRequiredMixin, generic.ListView):
    model = Cook
    context_object_name = "cooks"
    template_name = "cook_list.html"
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class CookDetailView(LoginRequiredMixin, generic.DetailView):
    model = Cook
    context_object_name = "cook"
    template_name = "cook_detail.html"


class CookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Cook
    form_class = CookCreationForm
    template_name = "cook_form.html"
    success_url = reverse_lazy("cook_list")


class CookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Cook
    form_class = CookUpdateForm
    template_name = "cook_form.html"
    success_url = reverse_lazy("cook_list")


class CookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Cook
    template_name = "cook_confirm_delete.html"
    success_url = reverse_lazy("cook_list")
