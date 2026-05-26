from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.contrib.auth.forms import UserCreationForm as DjangoUserCreationForms
from django.utils.translation import gettext_lazy as _

from .models import User


class UserCreationForm(DjangoUserCreationForms):
    class Meta(DjangoUserCreationForms.Meta):
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "employee_code",
            "role",
            "supervisor",
        )


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
        )


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": _("Usuario"),
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": _("Contraseña"),
            }
        )
    )
