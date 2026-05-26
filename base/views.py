from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
from django.views.generic import DetailView

from customers.models import (
    Customer,
)


class CustomerDetailView(LoginRequiredMixin, DetailView):
    model = Customer
    template_name = "base/customer_detail.html"
    context_object_name = "cliente"

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.role == user.Roles.SUPERVISOR:
            return self.model.objects.all()

        return self.model.objects.filter(seller=user)
