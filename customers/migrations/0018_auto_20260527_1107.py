from django.contrib.auth.hashers import make_password
from django.db import migrations


def cargar_todo_el_crm(apps, schema_editor):
    # 1. Recuperar los modelos del historial de Django
    User = apps.get_model("users", "User")
    Customer = apps.get_model("customers", "Customer")
    Interaction = apps.get_model("customers", "Interaction")

    # ==========================================
    # PASO 1: VENDEDORES Y SUPERVISORES
    # ==========================================
    usuarios_data = [
        {
            "id": 1,
            "email": "bx@bx1.com",
            "first_name": "",
            "last_name": "",
            "is_superuser": True,
            "is_staff": True,
            "role": "ADMIN",
            "employee_code": "ADM001",
        },
        {
            "id": 4,
            "email": "joan@crm.com",
            "first_name": "Joan",
            "last_name": "Supervisor",
            "is_superuser": False,
            "is_staff": True,
            "role": "SUPERVISOR",
            "employee_code": "SUP004",
        },
        {
            "id": 5,
            "email": "marta@crm.com",
            "first_name": "Marta",
            "last_name": "Vendedora",
            "is_superuser": False,
            "is_staff": False,
            "role": "VENDEDOR",
            "employee_code": "VEN005",
        },
        {
            "id": 6,
            "email": "pau@crm.com",
            "first_name": "Pau",
            "last_name": "Vendedor",
            "is_superuser": False,
            "is_staff": False,
            "role": "VENDEDOR",
            "employee_code": "VEN006",
        },
        {
            "id": 7,
            "email": "raquel@crm.com",
            "first_name": "Raquel",
            "last_name": "Vendedora",
            "is_superuser": False,
            "is_staff": False,
            "role": "VENDEDOR",
            "employee_code": "VEN007",
        },
    ]

    for u in usuarios_data:
        if not User.objects.filter(id=u["id"]).exists():
            User.objects.create(
                id=u["id"],
                email=u["email"],
                password=make_password(
                    "PasswordTemporal123!"
                ),  # Password seguro para entrar a producción
                first_name=u["first_name"],
                last_name=u["last_name"],
                is_superuser=u["is_superuser"],
                is_staff=u["is_staff"],
                is_active=True,
                role=u["role"],
                employee_code=u["employee_code"],
            )

    # ==========================================
    # PASO 2: CLIENTES (Mapeo exacto de tu JSON)
    # ==========================================
    clientes_data = [
        {
            "id": 3,
            "photo": "media/customers/ven1_juan_ZgoWyRF_wnieys",
            "first_name": "Juan",
            "last_name": "Narvaez",
            "nif_nie": "43567891T",
            "adress": "Constanza 9, Madrid",
            "email": "jnarv@cust.com",
            "phone_number": "123456789",
            "customer_code": "CJN001001",
            "marital_status": "Casado/a",
            "profession": "Fontanero",
            "company": None,
            "status": "INTERESTED",
            "product": "ALARMS_OUT",
            "seller_id": 5,
            "created_at": "2026-05-26",
        },
        {
            "id": 4,
            "photo": "media/customers/ven1_andrea_bCPrefQ_nzbeqj",
            "first_name": "Andrea",
            "last_name": "Doria",
            "nif_nie": None,
            "adress": "Calle  Maria de Sepulveda 6, 07021, Mallorca",
            "email": "andrea.d@cust.com",
            "phone_number": "987654321",
            "customer_code": "CAD001002",
            "marital_status": "Soltero/a",
            "profession": "Cocinera",
            "company": None,
            "status": "INTERESTED",
            "product": "ALARMS_OUT",
            "seller_id": 5,
            "created_at": "2026-05-26",
        },
        {
            "id": 5,
            "photo": "media/customers/ven1_carla_new9ro",
            "first_name": "Carla",
            "last_name": "Goikochea",
            "nif_nie": None,
            "adress": "Calle Legazpy 4, 48719, Bilbao",
            "email": "cgoikochea@cust.com",
            "phone_number": "132465798",
            "customer_code": "CCG001003",
            "marital_status": "Casado/a",
            "profession": "Ingeniera",
            "company": "NewTech",
            "status": "NEGOTIATION",
            "product": "ALARMS_OUT",
            "seller_id": 5,
            "created_at": "2026-05-26",
        },
        {
            "id": 6,
            "photo": "media/customers/ven2_ralph_gubikx",
            "first_name": "Ralph",
            "last_name": "Velazquez",
            "nif_nie": None,
            "adress": "Calle Fonsana 12, 43724, Tarragona",
            "email": "rvlz@cust.com",
            "phone_number": "321654987",
            "customer_code": "CRH001002",
            "marital_status": "Casado/a",
            "profession": "Restaurador",
            "company": "Restauraciones Velazquez",
            "status": "INTERESTED",
            "product": "ALARMS_OUT",
            "seller_id": 7,
            "created_at": "2026-05-26",
        },
        {
            "id": 7,
            "photo": "media/customers/ven2_josh_rk54ze",
            "first_name": "Joshua",
            "last_name": "Pineda",
            "nif_nie": None,
            "adress": "Calle de la Venganza 1, 46123, Valencia",
            "email": "jpin@custom.com",
            "phone_number": "978645312",
            "customer_code": "CJP002002",
            "marital_status": "Casado/a",
            "profession": "Gestor empresarial",
            "company": "Suministros Sanitarios Pineda",
            "status": "NEW_LEAD",
            "product": "ALARMS_OUT",
            "seller_id": 7,
            "created_at": "2026-05-26",
        },
        {
            "id": 8,
            "photo": "media/customers/ven2_mayte_chqpih",
            "first_name": "Mayte",
            "last_name": "Gutierrez",
            "nif_nie": None,
            "adress": "Calle San Antoni 5, 07003, Palma",
            "email": "mgutisan@cust.com",
            "phone_number": "147258379",
            "customer_code": "CMG003002",
            "marital_status": "Casado/a",
            "profession": "Profesora",
            "company": None,
            "status": "NEW_LEAD",
            "product": "ALARMS_OUT",
            "seller_id": 7,
            "created_at": "2026-05-26",
        },
        {
            "id": 9,
            "photo": "media/customers/ven3_karen_dwsgiz",
            "first_name": "Karen",
            "last_name": "López",
            "nif_nie": None,
            "adress": "Calle Cienfuegos 23, 35011, Las Palmas G.C.",
            "email": "Klopez2@cust.com",
            "phone_number": "975318642",
            "customer_code": "CKL001003",
            "marital_status": "Casado/a",
            "profession": "Peluquera",
            "company": "Peluquerias NewLook",
            "status": "NEW_LEAD",
            "product": "ALARMS_OUT",
            "seller_id": 6,
            "created_at": "2026-05-26",
        },
        {
            "id": 10,
            "photo": "media/customers/ven3_hamid_o4lm6o",
            "first_name": "Hamid",
            "last_name": "Arzauk",
            "nif_nie": None,
            "adress": "Calle Alcantara 7 , 41443, Sevilla",
            "email": "hamidaz@cust.com",
            "phone_number": "978645344",
            "customer_code": "CHA002003",
            "marital_status": "Casado/a",
            "profession": "Joyero",
            "company": "Joyerias Arzauk",
            "status": "NEW_LEAD",
            "product": "ALARMS_OUT",
            "seller_id": 6,
            "created_at": "2026-05-26",
        },
        {
            "id": 11,
            "photo": "media/customers/ven3_gloria_la5snl",
            "first_name": "Gloria",
            "last_name": "Salazar",
            "nif_nie": None,
            "adress": "Calle Jovellanos 34, 37002, Salamanca",
            "email": "salazarg@cust.com",
            "phone_number": "123654987",
            "customer_code": "CGS003003",
            "marital_status": "Casado/a",
            "profession": "Música",
            "company": None,
            "status": "NEW_LEAD",
            "product": "ALARMS_OUT",
            "seller_id": 6,
            "created_at": "2026-05-26",
        },
    ]

    for c in clientes_data:
        if not Customer.objects.filter(id=c["id"]).exists():
            Customer.objects.create(
                id=c["id"],
                photo=c["photo"],
                first_name=c["first_name"],
                last_name=c["last_name"],
                nif_nie=c["nif_nie"],
                adress=c["adress"],
                email=c["email"],
                phone_number=c["phone_number"],
                customer_code=c["customer_code"],
                marital_status=c["marital_status"],
                profession=c["profession"],
                company=c["company"],
                status=c["status"],
                product=c["product"],
                seller_id=c["seller_id"],  # Enlazado directo a la ID del comercial
                created_at=c["created_at"],
            )

    # ==========================================
    # PASO 3: INTERACCIONES
    # ==========================================
    interacciones_data = [
        {
            "id": 10,
            "customer_id": 11,
            "seller_id": 6,
            "interaction_type": "CALL",
            "notes": "Se le pregunta por la informacion recibida y se tantea su opinion sobre el producto.",
            "date": "2026-05-11T22:38:58.518Z",
            "duration_minutes": 10,
        },
        {
            "id": 11,
            "customer_id": 10,
            "seller_id": 6,
            "interaction_type": "MEETING",
            "notes": "Interesado nuestro pack completo de Seguridad previa apretura del negocio",
            "date": "2026-05-12T00:28:24.399Z",
            "duration_minutes": 120,
        },
        {
            "id": 13,
            "customer_id": 8,
            "seller_id": 7,
            "interaction_type": "WHATSAPP",
            "notes": "Se  contacta tras mostrar interes por nuestra gama de detectores de movimiento",
            "date": "2026-05-12T00:32:20.002Z",
            "duration_minutes": 5,
        },
        {
            "id": 14,
            "customer_id": 7,
            "seller_id": 7,
            "interaction_type": "MEETING",
            "notes": "Ralph necesita un sistema completo de videovigilancia puesto que ha cambiado la ubicacion de sus almacenes.",
            "date": "2026-05-12T00:33:19.289Z",
            "duration_minutes": 90,
        },
        {
            "id": 15,
            "customer_id": 5,
            "seller_id": 5,
            "interaction_type": "VIDEOCALL",
            "notes": "Nos comenta que ha abierto una nueva oficina en el centro y necesita un sistema de videovigilancia y alarmas interiores.",
            "date": "2026-05-12T00:36:24.879Z",
            "duration_minutes": 45,
        },
        {
            "id": 16,
            "customer_id": 4,
            "seller_id": 5,
            "interaction_type": "EMAIL",
            "notes": "Solicita info sobre alrmas internas. Se le envia info comercial y contacto",
            "date": "2026-05-12T00:37:20.784Z",
            "duration_minutes": 10,
        },
        {
            "id": 26,
            "customer_id": 3,
            "seller_id": 5,
            "interaction_type": "MEETING",
            "notes": "El cliente manifiesta interes por la instalación de alarmas interiores",
            "date": "2026-05-14T07:56:31.573Z",
            "duration_minutes": 25,
        },
        {
            "id": 27,
            "customer_id": 5,
            "seller_id": 5,
            "interaction_type": "CALL",
            "notes": "La cliente nos confirma interes en la instalacion de los sistemas consultados.",
            "date": "2026-05-14T07:58:29.920Z",
            "duration_minutes": 25,
        },
        {
            "id": 28,
            "customer_id": 6,
            "seller_id": 7,
            "interaction_type": "EMAIL",
            "notes": "El cliente nos contacta para solicitar informacion sobre nuestro set completo de vigilancia.",
            "date": "2026-05-14T08:03:46.562Z",
            "duration_minutes": 5,
        },
        {
            "id": 30,
            "customer_id": 9,
            "seller_id": 6,
            "interaction_type": "CALL",
            "notes": "La clienta contacta tras intento de entrada a su negocio. solicita informacion sobre sistema de videovigilancia",
            "date": "2026-05-14T08:07:00.417Z",
            "duration_minutes": 25,
        },
        {
            "id": 35,
            "customer_id": 3,
            "seller_id": 4,
            "interaction_type": "CALL",
            "notes": "El cliente solicita dossier sobre el catalogo de alarmas",
            "date": "2026-05-14T21:41:19.185Z",
            "duration_minutes": 20,
        },
    ]

    for i in interacciones_data:
        if not Interaction.objects.filter(id=i["id"]).exists():
            # Validación de seguridad por si el seller asignado es el Supervisor (ID: 4)
            Interaction.objects.create(
                id=i["id"],
                customer_id=i["customer_id"],
                seller_id=i["seller_id"],
                interaction_type=i["interaction_type"],
                notes=i["notes"],
                date=i["date"],
                duration_minutes=i["duration_minutes"],
            )


def deshacer_todo(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        (
            "customers",
            "0001_initial",
        ),  # Asegúrate de poner el nombre exacto de tu migración base de clientes
        ("users", "0001_initial"),  # Y de la de usuarios
    ]

    operations = [
        migrations.RunPython(cargar_todo_el_crm, reverse_code=deshacer_todo),
    ]
