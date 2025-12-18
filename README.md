# Proyecto 1: CI/CD con GitHub Actions + Terraform + Docker

**Equipo 02 - PIN MundosE**

Proyecto de DevOps que implementa un pipeline CI/CD completo para una aplicación Django, incluyendo infraestructura como código con Terraform, contenedorización con Docker, análisis de seguridad, generación de SBOM y monitoreo con Prometheus y Grafana.

---

## 📋 Tabla de Contenidos

- [Descripción](#descripción)
- [Tecnologías](#tecnologías)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Requisitos Previos](#requisitos-previos)
- [Instalación y Configuración](#instalación-y-configuración)
- [CI/CD Pipeline](#cicd-pipeline)
- [Monitoreo](#monitoreo)
- [Terraform](#terraform)
- [Tests](#tests)
- [Seguridad](#seguridad)
- [SBOM](#sbom)
- [Uso del Proyecto](#uso-del-proyecto)
- [Entregables](#entregables)

---

## 📖 Descripción

Este proyecto implementa una solución completa de DevOps para una aplicación Django que incluye:

- **Pipeline CI/CD automatizado** con GitHub Actions
- **Infraestructura como código** con Terraform
- **Contenedorización** con Docker
- **Análisis de seguridad** con Snyk y SonarCloud
- **Generación automática de SBOM** (Software Bill of Materials)
- **Monitoreo** con Prometheus y Grafana
- **Tests automatizados** con Django Test Framework

---

## 🛠️ Tecnologías

### Backend
- **Python 3.11**
- **Django 5.2.9**
- **Pillow** (procesamiento de imágenes)
- **django-prometheus** (métricas)

### DevOps
- **GitHub Actions** - CI/CD Pipeline
- **Docker** - Contenedorización
- **Docker Compose** - Orquestación de servicios
- **Terraform** - Infraestructura como código

### Seguridad
- **Snyk** - Análisis de vulnerabilidades en dependencias
- **SonarCloud** - Análisis estático de código

### Monitoreo
- **Prometheus** - Recopilación de métricas
- **Grafana** - Visualización y dashboards

### Herramientas
- **CycloneDX** - Generación de SBOM

---

## 📁 Estructura del Proyecto

```
mundosEPIN_Equipo02-main/
├── .github/
│   └── workflows/
│       └── ci-cd.yml          # Pipeline de CI/CD
├── app/                        # Aplicación Django
│   ├── App3D/                  # App principal
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   └── tests.py           # Tests unitarios
│   ├── ProyectoBlog/           # Configuración Django
│   │   ├── settings.py
│   │   └── urls.py
│   ├── Dockerfile              # Imagen Docker
│   ├── requirements.txt       # Dependencias Python
│   └── manage.py
├── terraform/
│   └── main.tf                 # Configuración Terraform
├── prometheus/
│   └── prometheus.yml          # Configuración Prometheus
├── grafana/
│   └── provisioning/          # Configuración Grafana
│       ├── datasources/
│       └── dashboards/
├── docker-compose.yml          # Orquestación de servicios
├── sonar-project.properties    # Configuración SonarCloud
└── README.md                   # Esta documentación
```

---

## ✅ Requisitos Previos

### Software Necesario
- **Docker Desktop** (o Docker Engine + Docker Compose)
- **Terraform** (opcional, para pruebas locales)
- **Python 3.11** (opcional, para desarrollo local)
- **Git** (para clonar el repositorio)

### Cuentas y Tokens
- **GitHub** - Repositorio con GitHub Actions habilitado
- **SonarCloud** - Token de acceso (configurar como secret `SONAR_TOKEN`)
- **Snyk** - Token de acceso (configurar como secret `SNYK_TOKEN`)

---

## 📦 Instalación y Configuración

### 1. Clonar el Repositorio

```bash
git clone <url-del-repositorio>
cd mundosEPIN_Equipo02-main
```

### 2. Configurar Secrets en GitHub

Ve a **Settings → Secrets and variables → Actions** y agrega:

- `SONAR_TOKEN`: Token de SonarCloud
  - Obtener en: https://sonarcloud.io → My Account → Security
- `SNYK_TOKEN`: Token de Snyk
  - Obtener en: https://app.snyk.io → Account Settings → API Token

### 3. Configurar SonarCloud

El archivo `sonar-project.properties` ya está configurado con:
- **Project Key**: `andreskim4_mundosEPIN_Equipo02`
- **Organization**: `andreskim4`

Si necesitas cambiar estos valores, edita `sonar-project.properties`.

---

## 🔄 CI/CD Pipeline

El pipeline se ejecuta automáticamente en cada push y pull request a la rama `main`.

### Flujo del Pipeline

1. **Checkout del código**
2. **Setup de Python 3.11**
3. **Instalación de dependencias del sistema** (Pillow)
4. **Instalación de dependencias Python**
5. **Generación de SBOM** (CycloneDX)
6. **Análisis de seguridad con Snyk**
7. **Django check** (validación de configuración)
8. **Verificación de migraciones** (dry-run)
9. **Ejecución de tests**
10. **Análisis de código con SonarCloud**
11. **Build de imagen Docker**
12. **Validación de Terraform** (init + validate)

### Ver el Pipeline

- Ve a la pestaña **Actions** en GitHub
- Selecciona el workflow **CI/CD Django App**
- Revisa los logs de cada paso

---

## 📊 Monitoreo

El proyecto incluye monitoreo completo con Prometheus y Grafana.

### Levantar los Servicios

```bash
docker-compose up -d
```

### Acceder a los Servicios

- **Django App**: http://localhost:8000
- **Prometheus**: http://localhost:9090
- **Grafana**: http://localhost:3000
  - Usuario: `admin`
  - Contraseña: `admin`

### Métricas Disponibles

La aplicación Django expone métricas en `/metrics`:

- `django_http_requests_total` - Total de requests HTTP
- `django_http_request_duration_seconds` - Duración de requests
- `django_http_responses_total` - Total de respuestas por status code

### Dashboard de Grafana

El dashboard **"Django Application Metrics"** se carga automáticamente e incluye:

- **HTTP Requests Total** - Gráfico de requests por método y status
- **HTTP Request Duration** - Duración de requests
- **Active Users** - Estadística de usuarios activos
- **Response Status Codes** - Distribución de códigos de respuesta

### Generar Tráfico para Ver Métricas

```bash
# Hacer peticiones a la aplicación
curl http://localhost:8000/
curl http://localhost:8000/App3D/login/
curl http://localhost:8000/metrics  # Ver métricas directamente
```

---

## 🏗️ Terraform

### Configuración

El proyecto incluye configuración de Terraform para gestionar la infraestructura Docker.

**Archivo**: `terraform/main.tf`

### Recursos Definidos

- **docker_image**: Imagen Docker de la aplicación
- **docker_container**: Contenedor de la aplicación Django

### Validación en CI/CD

El pipeline valida automáticamente la configuración de Terraform:

```yaml
- terraform init -backend=false
- terraform validate
```

### Uso Local (Opcional)

```bash
cd terraform
terraform init
terraform plan
terraform apply
```

**Nota**: La imagen Docker debe estar construida antes de ejecutar `terraform apply`.

---

## 🧪 Tests

### Tests Implementados

El proyecto incluye 6 tests unitarios en `app/App3D/tests.py`:

1. **BlogModelTest**
   - `test_blog_creation` - Verifica creación de blogs

2. **CanalModelTest**
   - `test_canal_creation` - Verifica creación de canales
   - `test_canal_mensaje_creation` - Verifica creación de mensajes

3. **ViewsTest**
   - `test_login_view` - Verifica vista de login
   - `test_register_view` - Verifica vista de registro
   - `test_leer_blogs_view` - Verifica vista de blogs

### Ejecutar Tests Localmente

```bash
cd app
python manage.py test --verbosity=2
```

O usando el script:

```powershell
.\run_tests.ps1
```

### Tests en CI/CD

Los tests se ejecutan automáticamente en el pipeline con `continue-on-error: true` para no bloquear el build.

---

## 🔒 Seguridad

### Snyk

Análisis de vulnerabilidades en dependencias Python.

**Configuración**:
- Se ejecuta en el pipeline automáticamente
- Requiere `SNYK_TOKEN` como secret
- Analiza `requirements.txt`

**Ver resultados**: Revisa los logs del step "Snyk - Análisis de seguridad" en GitHub Actions.

### SonarCloud

Análisis estático de código para detectar bugs, vulnerabilidades y code smells.

**Configuración**:
- Archivo: `sonar-project.properties`
- Se ejecuta en el pipeline automáticamente
- Requiere `SONAR_TOKEN` como secret

**Ver resultados**: https://sonarcloud.io/summary/overall?id=andreskim4_mundosEPIN_Equipo02

---

## 📦 SBOM (Software Bill of Materials)

### Generación Automática

El SBOM se genera automáticamente en el pipeline usando **CycloneDX**.

**Formato**: CycloneDX 1.6 (JSON)

**Contenido**:
- Lista de dependencias (Django, Pillow)
- Versiones y PURLs
- Referencias externas

### Ubicación

- **Generado en**: Raíz del proyecto (`sbom.json`)
- **Subido como artefacto**: Disponible en GitHub Actions

### Ver el SBOM

1. Ve a **Actions** en GitHub
2. Selecciona un workflow run
3. Descarga el artefacto **sbom**

---

## 🚀 Uso del Proyecto

### Desarrollo Local

1. **Clonar el repositorio**
2. **Instalar dependencias**:
   ```bash
   cd app
   pip install -r requirements.txt
   ```
3. **Ejecutar migraciones**:
   ```bash
   python manage.py migrate
   ```
4. **Ejecutar servidor**:
   ```bash
   python manage.py runserver
   ```

### Con Docker

1. **Construir la imagen**:
   ```bash
   cd app
   docker build -t django-app:latest .
   ```

2. **Ejecutar el contenedor**:
   ```bash
   docker run -p 8000:8000 django-app:latest
   ```

### Con Docker Compose (Monitoreo Completo)

```bash
docker-compose up -d
```

Esto levanta:
- Django App (puerto 8000)
- Prometheus (puerto 9090)
- Grafana (puerto 3000)

---

## 📋 Entregables

### Archivos Incluidos

✅ **Workflow.yml** - `.github/workflows/ci-cd.yml`  
✅ **Archivos Terraform** - `terraform/main.tf`  
✅ **Dockerfile** - `app/Dockerfile`  
✅ **SBOM** - Generado automáticamente (CycloneDX)  
⚠️ **Screenshot del Dashboard** - Debe tomarse manualmente desde Grafana

### Cómo Obtener el Screenshot

1. Levantar servicios: `docker-compose up -d`
2. Acceder a Grafana: http://localhost:3000
3. Ir al dashboard "Django Application Metrics"
4. Generar tráfico a la aplicación
5. Tomar screenshot del dashboard con métricas

---

## 🔧 Configuración Adicional

### Variables de Entorno

El proyecto usa las siguientes variables (configuradas en `docker-compose.yml`):

- `DEBUG=True` - Modo debug de Django

### Puertos Utilizados

- **8000** - Django App
- **9090** - Prometheus
- **3000** - Grafana

### Redes Docker

Todos los servicios están en la red `monitoring` para comunicación interna.

---

## 📝 Notas Importantes

1. **Secrets de GitHub**: Asegúrate de configurar `SONAR_TOKEN` y `SNYK_TOKEN` antes de hacer push.

2. **Primera ejecución**: El pipeline puede fallar la primera vez si los secrets no están configurados. Esto es normal.

3. **Monitoreo**: Para ver métricas reales, genera tráfico a la aplicación Django después de levantar los servicios.

4. **Grafana**: El dashboard se carga automáticamente, pero puede tardar unos minutos en aparecer datos.

---

## 👥 Equipo

**Equipo 02 – PIN MundosE**

🔗 **Resultados de GitHub Actions:**  
👉 https://github.com/andreskim4/mundosEPIN_Equipo02/actions

### Integrantes
- Sueldo Roberto Luis  
- Gabriel Salatino  
- Gabriel Altamirano  
- Andres Kim

---

## 📄 Licencia

Este proyecto es parte de un trabajo práctico académico.

---

## 🔗 Enlaces Útiles

- [Documentación Django](https://docs.djangoproject.com/)
- [Docker Documentation](https://docs.docker.com/)
- [Terraform Documentation](https://www.terraform.io/docs)
- [Prometheus Documentation](https://prometheus.io/docs/)
- [Grafana Documentation](https://grafana.com/docs/)
- [SonarCloud](https://sonarcloud.io/)
- [Snyk](https://snyk.io/)

---

**Última actualización**: Diciembre 2025
