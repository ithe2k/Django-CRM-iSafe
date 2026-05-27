from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.db import connection
from django.urls import include, path

from users.views import UserLoginView


def reparar_tabla_usuario_completa():
    try:
        with connection.cursor() as cursor:
            print("--- COMPROBANDO Y REPARANDO ESTRUCTURA DE CRM_USER EN RENDER ---")

            # 1. Asegurar campos nativos de AbstractUser
            cursor.execute(
                "ALTER TABLE crm_user ADD COLUMN IF NOT EXISTS username VARCHAR(150) UNIQUE;"
            )
            cursor.execute(
                "ALTER TABLE crm_user ADD COLUMN IF NOT EXISTS password VARCHAR(128);"
            )
            cursor.execute(
                "ALTER TABLE crm_user ADD COLUMN IF NOT EXISTS is_active BOOLEAN DEFAULT TRUE;"
            )
            cursor.execute(
                "ALTER TABLE crm_user ADD COLUMN IF NOT EXISTS is_staff BOOLEAN DEFAULT FALSE;"
            )
            cursor.execute(
                "ALTER TABLE crm_user ADD COLUMN IF NOT EXISTS is_superuser BOOLEAN DEFAULT FALSE;"
            )
            cursor.execute(
                "ALTER TABLE crm_user ADD COLUMN IF NOT EXISTS date_joined TIMESTAMP WITH TIME ZONE DEFAULT NOW();"
            )
            cursor.execute(
                "ALTER TABLE crm_user ADD COLUMN IF NOT EXISTS first_name VARCHAR(150) DEFAULT '';"
            )
            cursor.execute(
                "ALTER TABLE crm_user ADD COLUMN IF NOT EXISTS last_name VARCHAR(150) DEFAULT '';"
            )
            cursor.execute(
                "ALTER TABLE crm_user ADD COLUMN IF NOT EXISTS email VARCHAR(254) DEFAULT '';"
            )

            cursor.execute(
                "ALTER TABLE crm_user ADD COLUMN IF NOT EXISTS role VARCHAR(20) DEFAULT 'SELLER';"
            )
            cursor.execute(
                "ALTER TABLE crm_user ADD COLUMN IF NOT EXISTS employee_code VARCHAR(10) UNIQUE;"
            )
            cursor.execute(
                "ALTER TABLE crm_user ADD COLUMN IF NOT EXISTS supervisor_id INTEGER NULL;"
            )

            print("--- ESTRUCTURA DE CRM_USER SANEADA CON ÉXITO ---")
    except Exception as e:
        print(f"Error al reparar la tabla: {e}")


reparar_tabla_usuario_completa()


def asegurar_usuario_admin():
    try:
        User = get_user_model()

        if not User.objects.filter(username="admin_username").exists():
            print("--- INYECTANDO USUARIO ADMINISTRADOR EN PRODUCTION ---")
            User.objects.create_superuser(
                username="bx_admin1",
                email="admin@ejemplo.com",
                password="proyect123",
                role="ADMIN",
                employee_code="ADM001",
            )
            print("--- USUARIO CREADO CON ÉXITO ---")
    except Exception as e:
        print(f"Error al inyectar el usuario: {e}")


asegurar_usuario_admin()

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", UserLoginView.as_view(), name="login"),
    path("users/", include("users.urls")),
    path("", include("base.urls")),
    path("customers/", include("customers.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
