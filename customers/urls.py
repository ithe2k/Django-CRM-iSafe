from django.urls import path

from . import views

app_name = "customers"

urlpatterns = [
    path("nuevo/", views.CustomerCreateView.as_view(), name="customer_create"),
    path(
        "<int:pk>/editar/", views.CustomerUpdateView.as_view(), name="customer_update"
    ),
    path(
        "<int:pk>/eliminar/", views.CustomerDeleteView.as_view(), name="customer_delete"
    ),
    path(
        "cliente/<int:pk>/nueva-interaccion/",
        views.InteractionCreateView.as_view(),
        name="interaction_create",
    ),
    path(
        "interaccion/<int:pk>/editar/",
        views.InteractionUpdateView.as_view(),
        name="interaction_update",
    ),
    path(
        "interaccion/<int:pk>/eliminar/",
        views.InteractionDeleteView.as_view(),
        name="interaction_delete",
    ),
]
