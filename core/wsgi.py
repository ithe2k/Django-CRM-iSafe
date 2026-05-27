import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# Levantar la aplicación de Django obligatoria
application = get_wsgi_application()

# --- PARCHE DE EMERGENCIA DE GUERRILLA ---
try:
    from django.core.management import call_command
    print("🤖 INTENTANDO INYECTAR DATOS DESDE WSGI...")
    call_command('loaddata', 'datos_produccion.json')
    print("🎉 ¡ÉXITO TOTAL! DATOS CARGADOS EN NEON.")
except Exception as e:
    import traceback
    print("❌ ERROR CRÍTICO CARGANDO JSON:")
    print(traceback.format_exc())
# ------------------------------------------
