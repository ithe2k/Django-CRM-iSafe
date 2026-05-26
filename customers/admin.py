from django.contrib import admin

from .models import Customer, Interaction


class InteractionInLine(admin.TabularInline):
    model = Interaction
    extra = 1
    fields = ("interaction_type", "notes", "duration_minutes")


@admin.register(Interaction)
class InteractionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "date",
        "customer",
        "seller",
        "interaction_type",
        "duration_minutes",
    )
    list_filter = ("interaction_type", "date", "seller")
    search_fields = (
        "customer__first_name",
        "customer__last_name",
        "notes",
    )


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        "first_name",
        "last_name",
        "company",
        "email",
        "phone_number",
        "seller",
        "created_at",
    )

    list_filter = ("status", "seller", "created_at", "product")

    search_fields = ("first_name", "last_name", "company", "email", "seller")

    fieldsets = (
        (
            "Información Personal",
            {
                "fields": (
                    "photo",
                    "customer_code",
                    ("first_name", "last_name"),
                    "email",
                    "phone_number",
                    "adress",
                    "marital_status",
                    "status",
                )
            },
        ),
        ("Información de Empresa", {"fields": ("company",)}),
        ("Asignación", {"fields": ("seller",)}),
    )

    readonly_fields = ["created_at"]

    inlines = [InteractionInLine]
