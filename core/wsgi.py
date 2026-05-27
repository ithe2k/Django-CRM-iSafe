import os
import sys
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_wsgi_application()

try:
    from django.core.management import call_command
    print("🤖 [WSGI] INICIANDO PROCESO DE CARGA SECUENCIAL...")
    
    # 1. Comprobamos si los archivos existen en el servidor de Render
    print(f"📁 Directorio actual: {os.getcwd()}")
    print(f"📁 Archivos disponibles: {os.listdir('.')}")
    
    # 2. Carga de usuarios
    print("🤖 [WSGI] Cargando test_users.json...")
    call_command('loaddata', 'users/fixtures/test_users.json')
    print("🎉 [WSGI] test_users.json cargado correctamente.")
    
    # 3. Carga de clientes
    print("🤖 [WSGI] Cargando clientes_e_interacciones.json...")
    call_command('loaddata', 'clientes_e_interacciones.json')
    print("🎉 [WSGI] ¡PROCESO COMPLETO SIN ERRORES EN PRODUCCIÓN!")

except Exception as e:
    print("❌ [WSGI] ¡ERROR CRÍTICO CAPTURADO EN LA INYECCIÓN!")
    import traceback
    traceback.print_exc(file=sys.stdout)  # Forzamos la salida directa al log de Render
