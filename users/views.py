from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from customers.models import Customer, Interaction

from .forms import LoginForm, UserCreationForm, UserUpdateForm
from .models import User


class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = "users/user_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["users"] = User.objects.all()
        return context

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.role == user.Roles.SUPERVISOR:
            return self.model.objects.all()

        return self.model.objects.filter(seller=user)


class UserDetailView(LoginRequiredMixin, DetailView):
    template_name = "users/user_detail.html"
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.kwargs.get("pk")
        context["user"] = User.objects.get(pk=user_id)
        return context

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.role == user.Roles.SUPERVISOR:
            return self.model.objects.all()

        return self.model.objects.filter(seller=user)


class SellerDetailView(LoginRequiredMixin, DetailView):
    template_name = "base/seller_detail.html"
    model = User
    context_object_name = "vendedor"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        vendedor = self.get_object()

        def get_queryset(self):
            if (
                self.request.user.is_superuser
                or self.request.user.groups.filter(name="Supervisor").exists()
            ):
                return self.model.objects.all()

            return self.model.objects.filter(seller=self.request.user)

        context["clientes_a_cargo"] = Customer.objects.filter(seller=vendedor)
        from django.db.models import Count, Sum

        stats = Interaction.objects.filter(seller=self.object).aggregate(
            total_tiempo=Sum("duration_minutes"), total_interacciones=Count("id")
        )
        context["stats"] = stats

        return context


class UserCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = User
    form_class = UserCreationForm
    template_name = "users/user_forms.html"
    success_message = "¡Usuario creado correctamente!"

    def get_success_url(self):
        return reverse("users:dashboard")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class UserUpdateView(
    LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView
):
    model = User
    form_class = UserUpdateForm
    template_name = "users/user_forms.html"

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.role == user.Roles.SUPERVISOR:
            return self.model.objects.all()

        return self.model.objects.filter(seller=user)

    def get_success_url(self):
        return reverse("users:dashboard")

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj or self.request.user.role in [
            "SUPERVISOR",
            "ADMIN",
        ]


class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = User

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj or self.request.user.role in [
            "SUPERVISOR",
            "ADMIN",
        ]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.role == user.Roles.SUPERVISOR:
            return self.model.objects.all()

        return self.model.objects.filter(seller=user)

    def get_success_url(self):
        messages.error(self.request, "¡Usuario eliminado correctamente!")
        return reverse("users:dashboard")


class UserLoginView(LoginView):
    template_name = "registration/login.html"
    authentication_form = LoginForm  #
    redirect_authenticated_user = True


class UserLogoutView(LogoutView):
    next_page = reverse_lazy("users:login")


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "base/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        q = self.request.GET.get("q", "").strip()

        context["es_admin"] = user.role == "ADMIN"
        context["es_supervisor"] = user.role == "SUPERVISOR"
        context["es_vendedor"] = user.role == "SELLER"

        base_clientes = Customer.objects.all()

        if user.role == "SUPERVISOR" or user.is_superuser:
            vendedores = User.objects.filter(role="SELLER")

            if q:
                vendedores = vendedores.filter(
                    Q(first_name__icontains=q)
                    | Q(last_name__icontains=q)
                    | Q(email__icontains=q)
                )

            context["vendedores"] = vendedores.order_by("-last_login")
            base_clientes = Customer.objects.all()

        elif user.role == "SELLER":
            base_clientes = Customer.objects.filter(seller=user)

            if q:
                base_clientes = base_clientes.filter(
                    Q(first_name__icontains=q)
                    | Q(last_name__icontains=q)
                    | Q(email__icontains=q)
                )
            context["avisos"] = self.generar_avisos(user)

        context["clientes_asignados"] = base_clientes.order_by("status")
        context["ultimas_interacciones"] = Interaction.objects.filter(
            customer__in=base_clientes
        ).order_by("-date")[:10]

        return context

    def generar_avisos(self, user):

        return []
