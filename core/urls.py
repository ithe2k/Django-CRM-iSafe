from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.db import connection
from django.urls import include, path

from users.views import UserLoginView


def reparar_tabla_usuario():
    try:
        with connection.cursor() as cursor:
            # Comprobamos si falta la columna username en el PostgreSQL de Render
            cursor.execute("""
                SELECT COUNT(*) 
                FROM information_schema.columns 
                WHERE table_name='crm_user' AND column_name='username';
            """)
            if cursor.fetchone()[0] == 0:
                print("--- REPARANDO COLUMNA USERNAME EN RENDER ---")
                cursor.execute(
                    "ALTER TABLE crm_user ADD COLUMN username VARCHAR(150) UNIQUE;"
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
    except Exception as e:
        print(f"Error al reparar la tabla: {e}")


# Ejecutar la reparación automática
reparar_tabla_usuario()

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", UserLoginView.as_view(), name="login"),
    path("users/", include("users.urls")),
    path("", include("base.urls")),
    path("customers/", include("customers.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
