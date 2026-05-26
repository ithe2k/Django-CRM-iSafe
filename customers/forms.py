from django import forms

from .models import Customer, Interaction


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = (
            "photo",
            "status",
            "first_name",
            "last_name",
            "nif_nie",
            "email",
            "phone_number",
            "adress",
            "company",
            "profession",
            "marital_status",
            "customer_code",
        )


class InteractionForm(forms.ModelForm):
    class Meta:
        model = Interaction
        fields = ["interaction_type", "duration_minutes", "notes"]
