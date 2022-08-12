from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.db.models import Sum
from django.contrib.contenttypes.fields import GenericRelation
from sharing.models import Share


class Budget(models.Model):
    """
    Budget that groups related items. 
    Each budget has items which can be managed. 
    """
    CURRENCY = (
        ('N', 'Naira'),
        ('$', 'US Dollar'),
    )
    name = models.CharField(max_length=70, unique=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    currency = models.CharField(max_length=1, choices=CURRENCY, default='N')
    shares = GenericRelation(Share)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('budget:detail', kwargs={'pk': self.pk})

    def get_total_cost(self):
        total_cost = self.item_set.all().filter(
            budget__id=self.id
        ).aggregate(total_cost=Sum('price'))
        return total_cost.get('total_cost')