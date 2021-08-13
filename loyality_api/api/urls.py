from django.urls import path

from api.views import AccountCreateView, AccountDetailView, AccountAllBalancesView, ActionCreateView

urlpatterns = [
    path("accounts/", AccountCreateView.as_view()),
    path("accounts/<int:pk>", AccountDetailView.as_view()),
    path("accounts/balances/", AccountAllBalancesView.as_view()),
    path("accounts/action/", ActionCreateView.as_view()),
]