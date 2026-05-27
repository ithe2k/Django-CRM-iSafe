import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_wsgi_application()

# --- CARGA EXCLUSIVA DE USUARIOS LIMPIOS ---
try:
    from django.core.management import call_command
    print("🤖 INYECTANDO EQUIPO DE VENTAS EN NEON...")
    call_command('loaddata', 'users/fixtures/test_users.json')
    print("🎉 ¡ÉXITO TOTAL! JOAN, MARTA, PAU Y RAQUEL ESTÁN DENTRO.")
except Exception as e:
    import traceback
    print("❌ ERROR EN LA INYECCIÓN:")
    print(traceback.format_exc())
