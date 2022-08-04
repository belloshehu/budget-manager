from django.shortcuts import render
from django.contrib.views import generic
from django.contrib.auth.mixins import LoginRequireMixin
from .models import Budget
from django.urls import reverse
from .forms import BudgetForm


class BudgteCreateView(LoginRequiredMixin, generic.CreateView):
    model = Budget
    form_class = BudgetForm

    def form_valid(self, form, *args, **kwargs):
        return super().form_valid(*args, **kwargs)



class BudgetListView(LoginRequireMixin, generic.ListView):
    model = Budget


class BudgetDetailView(LoginRequireMixin, generic.DetailView):
    model = Budget


class BudgetUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Budget
    form_class = BudgetForm

    def get_success_url(self):
        return reverse('dashboard: budget', kwargs={'pk':self.kwargs.get('pk')})


class BudgetDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Budget

    def get_success_url(self):
        return reverse('dashboard: budget')


