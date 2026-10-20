
"""
Django settings for config project.
"""

from pathlib import Path
import os
import dj_database_url


BASE_DIR = Path(__file__).resolve().parent.parent


# ==================================================
# CONFIGURACIÓN GENERAL
# ==================================================

SECRET_KEY = os.environ.get("SECRET_KEY")

if not SECRET_KEY:
    SECRET_KEY = "clave-solo-para-desarrollo-local"

DEBUG = os.environ.get("DEBUG", "False").lower() == "true"


# ==================================================
# DOMINIOS PERMITIDOS
# ==================================================

ALLOWED_HOSTS = [
    "solicitud1.vercel.app",
    ".vercel.app",
    "localhost",
    "127.0.0.1",
]

vercel_url = os.environ.get("VERCEL_URL", "").strip()

if vercel_url:
    ALLOWED_HOSTS.append(vercel_url)


# ==================================================
# ORÍGENES CONFIABLES PARA FORMULARIOS (CSRF)
# ==================================================

CSRF_TRUSTED_ORIGINS = [
    "https://solicitud1.vercel.app",
]

if vercel_url:
    CSRF_TRUSTED_ORIGINS.append(
        f"https://{vercel_url}"
        if not vercel_url.startswith("http")
        else vercel_url
    )

origenes_adicionales = os.environ.get(
    "CSRF_TRUSTED_ORIGINS", ""
)

for origen in origenes_adicionales.split(","):
    origen = origen.strip()
    if origen and origen not in CSRF_TRUSTED_ORIGINS:
        CSRF_TRUSTED_ORIGINS.append(origen)


# ==================================================
# COOKIES Y SEGURIDAD HTTPS
# ==================================================

CSRF_COOKIE_SECURE = not DEBUG
SESSION_COOKIE_SECURE = not DEBUG

CSRF_COOKIE_HTTPONLY = False
SESSION_COOKIE_HTTPONLY = True

SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"


# ==================================================
# APLICACIONES
# ==================================================

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "incidencias",
]


# ==================================================
# MIDDLEWARE
# ==================================================

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# ==================================================
# URLS Y APLICACIÓN
# ==================================================

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# ==================================================
# BASE DE DATOS: NEON POSTGRESQL
# ==================================================

DATABASE_URL = (
    os.environ.get("DATABASE_URL", "").strip()
    or os.environ.get(
        "abkenosolicitud_DATABASE_URL", ""
    ).strip()
)

if DATABASE_URL:
    DATABASES = {
        "default": dj_database_url.parse(
            DATABASE_URL,
            conn_max_age=0,
            ssl_require=True,
        )
    }
else:
    # SQLite solo para desarrollo local.
    # En Vercel configura DATABASE_URL en las variables
    # de entorno del proyecto.
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }


# ==================================================
# VALIDACIÓN DE CONTRASEÑAS
# ==================================================

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "UserAttributeSimilarityValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "MinimumLengthValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "CommonPasswordValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "CommonPasswordValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "NumericPasswordValidator"
        ),
    },
]


# ==================================================
# IDIOMA Y ZONA HORARIA
# ==================================================

LANGUAGE_CODE = "es-mx"

TIME_ZONE = "America/Mexico_City"

USE_I18N = True

USE_TZ = True


# ==================================================
# ARCHIVOS ESTÁTICOS
# ==================================================

STATIC_URL = "/static/"

STATIC_ROOT = BASE_DIR / "staticfiles"

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": (
            "whitenoise.storage.CompressedManifestStaticFilesStorage"
        ),
    },
}


# ==================================================
# MODELOS
# ==================================================

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# ==================================================
# INICIO Y CIERRE DE SESIÓN
# ==================================================

LOGIN_URL = "/accounts/login/"

LOGIN_REDIRECT_URL = "/"

LOGOUT_REDIRECT_URL = "/accounts/login/"