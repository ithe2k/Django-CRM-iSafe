from django.urls import path

from base.views import CustomerDetailView
from users.views import DashboardView

app_name = "base"  #

urlpatterns = [
    path("dashboard/", DashboardView.as_view(), name="dashboard"),
    path("cliente/<int:pk>/", CustomerDetailView.as_view(), name="customer_detail"),
]
