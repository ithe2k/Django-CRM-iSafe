from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.core.management import call_command
from django.http import HttpResponse
from django.urls import include, path

from users.views import UserLoginView


def ejecutar_carga_datos_en_vivo(request):
    try:
        # Forzamos la ejecución para ver qué pasa por detrás
        call_command("loaddata", "datos_produccion.json")
        return HttpResponse(
            "<h1>¡ÉXITO! Los datos se han cargado correctamente en Neon.</h1>"
        )
    except Exception:
        import traceback

        error_completo = traceback.format_exc()
        # Te escupe el Traceback real en el navegador
        return HttpResponse(
            f"<h3>Error al cargar el JSON:</h3><pre>{error_completo}</pre>", status=500
        )


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", UserLoginView.as_view(), name="login"),
    path("users/", include("users.urls")),
    path("", include("base.urls")),
    path("customers/", include("customers.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
