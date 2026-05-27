from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    class Roles(models.TextChoices):
        ADMIN = "ADMIN", _("Admin")
        SUPERVISOR = "SUPERVISOR", _("Supervisor/a")
        SELLER = "SELLER", _("Vendedor/a")

    role = models.CharField(
        max_length=20,
        choices=Roles.choices,
        default=Roles.SELLER,
        verbose_name=_("rol"),
    )

    employee_code = models.CharField(
        max_length=10,
        unique=True,
        verbose_name=_("código de empleado"),
        help_text=_("Código único de identificación interna"),
    )

    supervisor = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="vendedores_asignados",
        verbose_name=_("supervisor/a asignado/a"),
        help_text=_("Supervisor asignado a este vendedor"),
    )

    class Meta:
        db_table = "crm_user"
        verbose_name = _("usuario")
        verbose_name_plural = _("usuarios")

    def __str__(self):
        return f"{self.username} - {self.get_role_display()}"
