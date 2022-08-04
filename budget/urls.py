from django.shortcuts import path
import .views

app_name = 'budget'

urlpatterns = [
    path('', views.BudgteCreateView.as_view(), name='create'),
    path('list/', views.BudgetListView.as_view(), name='list'),
    path('detail/<int:pk>/', views.BudgetDetailView.as_view(), 'detail'),
    path('update/<int:pk>/', views.BudgetUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.BudgetDeleteView.as_view(), name='delete'),
]