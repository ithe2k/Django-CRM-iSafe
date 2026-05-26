from django.db import models
from django.utils.translation import gettext_lazy as _


class Customer(models.Model):
    photo = models.ImageField(upload_to="customers/", null=True, blank=True)
    first_name = models.CharField(_("Nombre"), max_length=50)
    last_name = models.CharField(_("Apellido"), max_length=50)
    nif_nie = models.CharField(null=True, blank=True)
    adress = models.CharField(_("Dirección"), max_length=150)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(_("Telefono"))
    customer_code = models.CharField(_("Codigo Cliente"), max_length=50)

    class Marital_Status(models.TextChoices):
        CASADO = "Casado/a", "Casado/a"
        SOLTERO = "Soltero/a", "Soltero/a"

    marital_status = models.CharField(
        max_length=20,
        choices=Marital_Status.choices,
        default=Marital_Status.SOLTERO,
        verbose_name=_("Estado Civil"),
    )

    profession = models.CharField(_("Profesión"), max_length=100)
    company = models.CharField(_("Empresa"), max_length=150, null=True, blank=True)

    class Status(models.TextChoices):
        NEW_LEAD = "NEW_LEAD", _("Nuevo Lead")
        INTERESTED = "INTERESTED", _("Interesado")
        NEGOTIATION = "NEGOTIATION", _("Negociación")
        WIN = "WIN", _("Activo")

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.NEW_LEAD,
        verbose_name=_("Estado"),
    )

    class Product(models.TextChoices):
        ALARMS_OUT = "ALARMS_OUT", _("Alarmas exteriores")
        ALARMS_IN = "ALARMS_IN", _("Alarmas interiores")
        VIDEO_SUR = "VIDEO_SUR", _("Video vigilancia")
        MOTION_DET = "MOTION_DET", _("Detector de Movimientos")
        FULL_PACK = "FULL_PACK", _("Paquete completo")

    product = models.CharField(
        max_length=50,
        choices=Product.choices,
        default=Product.ALARMS_OUT,
        verbose_name=_("Productos"),
    )

    class Meta:
        verbose_name = _("cliente")
        verbose_name_plural = _("clientes")

    def __str__(self):
        return self.first_name

    seller = models.ForeignKey(
        "users.User",
        verbose_name=_("Vendedor_Asignado"),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    created_at = models.DateField(
        _("Fecha de entrada"), auto_now=True, auto_now_add=False
    )


class Interaction(models.Model):
    class Type(models.TextChoices):
        CALL = "CALL", "Llamada Telefónica"
        EMAIL = "EMAIL", "Correo Electrónico"
        MEETING = "MEETING", "Reunión Presencial"
        WHATSAPP = "WHATSAPP", "Mensaje WhatsApp"
        VIDEOCALL = "VIDEOCALL", "Videollamada"
        default = "-"

    customer = models.ForeignKey(
        "customers.Customer",
        on_delete=models.CASCADE,
        related_name="interactions",
        default=1,
    )
    seller = models.ForeignKey("users.User", on_delete=models.CASCADE, default=1)

    interaction_type = models.CharField(
        max_length=20,
        choices=Type.choices,
        default=Type.CALL,
        verbose_name="Interacción",
    )
    notes = models.TextField(
        help_text="Resumen de lo hablado",
        default="Sin notas",
        verbose_name="Notas",
    )
    date = models.DateTimeField(auto_now_add=True)
    # Este campo es clave para las estadísticas que pides
    duration_minutes = models.PositiveIntegerField(
        default=0,
        verbose_name="Duaración",
    )

    def __str__(self):
        return f"{self.interaction_type} - {self.customer.last_name} ({self.date.strftime('%d/%m/%Y')})"
