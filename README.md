# iSafe CRM 🛡️
**Gestión inteligente de clientes y relaciones comerciales.**

iSafe es un sistema de gestión de relaciones con el cliente (CRM) desarrollado con **Django**, diseñado para optimizar el flujo de trabajo entre vendedores y supervisores. El proyecto pone un foco especial en la seguridad de los datos y la jerarquía de acceso.

## 🚀 Características Principales
- **Arquitectura de Roles:** Diferenciación clara entre Administrador, Supervisor y Vendedor.
- **Seguridad IDOR:** Protección de rutas para evitar que vendedores accedan a clientes ajenos.
- **Gestión de Interacciones:** Registro detallado de cada contacto con el cliente.
- **Panel de Control:** Dashboard dinámico con métricas clave según el rol de usuario.


## 🛠️ Stack Tecnológico
- **Backend:** Python 3.12 + Django 6.0
- **Base de Datos:** PostgreSQL
- **Entorno:** Docker & Docker Compose
- **Frontend:** Tailwind CSS v4 + Widget Tweaks
- **Seguridad:** Python-dotenv para gestión de variables de entorno.

Primer proyecto elaborado con Django en periodo formativo.

---

## 🔑 Credenciales de Acceso y Roles (Evaluación / QA)

Para facilitar la auditoría del CRM y permitir la comprobación de la jerarquía de permisos y la asignación de clientes, se incluye el archivo de datos simulados `users.json` (fixture). 

A continuación se detallan las cuentas preconfiguradas listas para usar:

### 👤 1. Administrador (Superuser)
* **Rol:** Acceso total al panel de control general
* **Código Empleado:** `ADM001`
* **Username:** `bx_admin1`
* **Email:** `bx@bx1.com`
* **Contraseña:** `proyect123`

### 👥 2. Supervisor de Equipo
* **Rol:** Joan Muntaner (Gestión de métricas del equipo y supervisión)
* **Código Empleado:** `SUP001`
* **Username:** `sup_joan`
* **Email:** `joan@sup.com`
* **Contraseña:** `sup12345`

### 💼 3. Asesores Comerciales (Vendedores)

* **Vendedor 1**
    * **Nombre:** Marta Diaz
    * **Código Empleado:** `VEN001`
    * **Username:** `ven1_marta`
    * **Email:** `marta@ven.com`
    * **Contraseña:** `marta12345`

* **Vendedor 2**
    * **Nombre:** Raquel Marquez
    * **Código Empleado:** `VEN002`
    * **Username:** `ven2_raquel`
    * **Email:** `raquel@ven.com`
    * **Contraseña:** `raquel12345`

* **Vendedor 3**
    * **Nombre:** Pau Ortell
    * **Código Empleado:** `VEN003`
    * **Username:** `ven3_pau`
    * **Email:** `pau@ven.com`
    * **Contraseña:** `pau12345`

---

### 📉 Estructura Jerárquica del Equipo
El usuario Joan Muntaner (`SUP001`) actúa como el supervisor directo en la base de datos de los tres asesores comerciales (Marta, Raquel y Pau). 

* Al iniciar sesión como **Supervisor**, el tribunal podrá auditar el rendimiento global del equipo.
* Al iniciar sesión con cualquiera de los **Vendedores**, la interfaz limitará automáticamente la vista mostrando únicamente su cartera exclusiva de clientes asignados.

### 📥 Cómo cargar estos usuarios
Si se despliega el proyecto sobre una base de datos limpia, se puede inyectar toda esta estructura ejecutando en la terminal:
```bash
python manage.py loaddata users

### 👥 Jerarquía del Equipo Comercial Configurada:
* **Joan Muntaner (`SUP001`)** actúa como el nodo supervisor directo en la base de datos para los tres vendedores (**Marta**, **Pau** y **Raquel**). 
* Iniciar sesión con el perfil de Joan permite auditar las métricas globales del equipo, mientras que las cuentas de los asesores comerciales limitan la vista a sus carteras de clientes asignadas de forma exclusiva.

### 📥 Cómo cargar estos usuarios en el entorno:
Si estás desplegando el proyecto en una base de datos limpia, puedes inyectar de golpe toda esta estructura ejecutando el siguiente comando en la terminal con el entorno virtual activo:
```bash
python manage.py loaddata users

## ☁️ Gestión de Archivos Multimedia (Cloudinary)

Para el almacenamiento y renderizado de las imágenes de las propiedades, este proyecto está integrado con **Cloudinary**, un servicio de gestión de medios en la nube. 

Se ha seleccionado esta arquitectura por los siguientes motivos técnicos:
* **Persistencia en Producción:** Evita la pérdida de imágenes al desplegar en servidores o plataformas (como Heroku o Render) cuyos sistemas de archivos son efímeros (se borran en cada reinicio).
* **Rendimiento e Infraestructura:** Las imágenes se sirven optimizadas a través de una red de entrega de contenido (CDN), reduciendo la carga en nuestro servidor Django.
* **Buenas Prácticas de Git:** Al delegar el almacenamiento a Cloudinary, evitamos saturar el repositorio de GitHub con archivos binarios pesados. La carpeta local de medios y el archivo de configuración `.env` se encuentran estrictamente protegidos en el `.gitignore`.

### Configuración requerida
Para que el sistema de carga múltiple funcione localmente, asegúrate de añadir tu credencial en el archivo `.env` en la raíz del proyecto (puedes guiarte con el archivo `.env.example`):

```env
CLOUDINARY_URL=cloudinary://<tu_api_key>:<tu_api_secret>@<tu_cloud_name>

## 🗄️ Base de Datos en Producción

El entorno de producción de este CRM utiliza una arquitectura de base de datos **PostgreSQL** totalmente gestionada en la nube a través de **Neon** (`neon.tech`), un servicio serverless de alto rendimiento optimizado para aplicaciones modernas. 

La conexión entre el Web Service de Render y la base de datos de Neon se realiza de forma segura mediante credenciales cifradas y exige de forma obligatoria el uso de conexiones protegidas por **SSL** (`sslmode=require`), garantizando la integridad y confidencialidad de todos los datos del CRM (usuarios, clientes e interacciones) en el entorno de despliegue.
