from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView

from .forms import CustomerForm, InteractionForm
from .models import Customer, Interaction


class CustomerCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = "customers/customer_forms.html"
    success_message = "¡Cliente registrado con éxito!"
    success_url = reverse_lazy("users:dashboard")

    def form_valid(self, form):
        form.instance.seller = self.request.user
        return super().form_valid(form)


class CustomerUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = "customers/customer_forms.html"
    success_message = "¡Datos del cliente actualizados!"
    success_url = reverse_lazy("users:dashboard")

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.role == user.Roles.SUPERVISOR:
            return self.model.objects.all()

        return self.model.objects.filter(seller=user)


class CustomerDeleteView(LoginRequiredMixin, DeleteView):
    model = Customer
    template_name = "customers/customer_confirm_delete.html"
    success_url = reverse_lazy("users:dashboard")

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.role == user.Roles.SUPERVISOR:
            return self.model.objects.all()

        return self.model.objects.filter(seller=user)


class InteractionCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Interaction
    form_class = InteractionForm
    template_name = "customers/interaction_forms.html"
    success_message = "¡Interacción registrada correctamente!"

    def form_valid(self, form):
        pk_cliente = self.kwargs.get("pk")
        user = self.request.user

        if user.is_superuser or user.role == user.Roles.SUPERVISOR:
            form.instance.customer = get_object_or_404(Customer, pk=pk_cliente)
        else:
            form.instance.customer = get_object_or_404(
                Customer, pk=pk_cliente, seller=user
            )

        form.instance.seller = user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy(
            "base:customer_detail", kwargs={"pk": self.object.customer.pk}
        )


class InteractionUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Interaction
    form_class = InteractionForm
    template_name = "customers/interaction_forms.html"
    success_message = "Interacción actualizada correctamente."

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.role == user.Roles.SUPERVISOR:
            return self.model.objects.all()

        else:
            return self.model.objects.filter(seller=user)

    def get_success_url(self):
        return reverse_lazy(
            "base:customer_detail", kwargs={"pk": self.object.customer.pk}
        )


class InteractionDeleteView(LoginRequiredMixin, DeleteView):
    model = Interaction
    template_name = "customers/interaction_confirm_delete.html"

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        from django.contrib import messages

        messages.success(request, "¡Interacción eliminada correctamente!")
        return response

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.role == user.Roles.SUPERVISOR:
            return self.model.objects.all()

        return self.model.objects.filter(seller=user)

    def get_success_url(self):
        return reverse_lazy(
            "base:customer_detail", kwargs={"pk": self.object.customer.pk}
        )
