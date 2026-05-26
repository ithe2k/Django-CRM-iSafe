# users/urls.py
from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("logout/", views.UserLogoutView.as_view(), name="logout"),
    path("dashboard/", views.DashboardView.as_view(), name="dashboard"),
    path("vendedores/", views.UserListView.as_view(), name="user_list"),
    path("vendedor/<int:pk>/", views.SellerDetailView.as_view(), name="seller_detail"),
    path("vendedor/nuevo/", views.UserCreateView.as_view(), name="user_create"),
    path(
        "vendedor/<int:pk>/editar/", views.UserUpdateView.as_view(), name="user_update"
    ),
    path(
        "vendedor/<int:pk>/eliminar/",
        views.UserDeleteView.as_view(),
        name="user_delete",
    ),
]
