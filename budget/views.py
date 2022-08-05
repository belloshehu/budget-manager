from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Budget
from django.urls import reverse
from .forms import BudgetForm
from django.db.models import Sum
from django.http import HttpResponseRedirect


class BudgetCreateView(LoginRequiredMixin, generic.CreateView):
    model = Budget
    form_class = BudgetForm

    def form_valid(self, form, *args, **kwargs):
        form.instance.owner = self.request.user
        form.save()
        return super().form_valid(form, *args, **kwargs)


class BudgetListView(LoginRequiredMixin, generic.ListView):
    model = Budget


class BudgetDetailView(LoginRequiredMixin, generic.DetailView):
    model = Budget

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     context.update(self.get_total_cost())
    #     return context

    # def get_total_cost(self):
    #     """
    #     Returns the sum of cost of all items in a budget.
    #     """
    #     total_cost = self.get_object().item_set.all().aggregate(total_cost=Sum('price'))
    #     return total_cost


class BudgetUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Budget
    form_class = BudgetForm
    template_name = 'budget/budget_update_form.html'

    def get_success_url(self):
        return reverse('budget:detail', kwargs={'pk':self.kwargs.get('pk')})


class BudgetDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Budget

    def get_success_url(self):
        return HttpResponseRedirect(reverse('custom_account:budgets'))


