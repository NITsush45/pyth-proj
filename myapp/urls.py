from django.urls import path
from .views import BranchListView, home

urlpatterns = [
    path('', home, name='home'),
    path('banks/', views.BankList.as_view(), name='bank-list'),
    path('branches/', BranchListView.as_view(), name='branch-list'),
]
