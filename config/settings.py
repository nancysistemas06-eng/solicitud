
import os
from pathlib import Path

import dj_database_url


# ==========================================================
# RUTAS DEL PROYECTO
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent.parent


# ==========================================================
# SEGURIDAD
# ==========================================================

SECRET_KEY = os.environ.get(
    "SECRET_KEY",
    "clave-solo-para-desarrollo-local"
)

DEBUG = os.environ.get("DEBUG", "False").lower() in ("true", "1", "yes")

ALLOWED_HOSTS = [
    "solicitud1.vercel.app",
    "solicitud1-b5pnc4vmr-abkeno.vercel.app",
    ".vercel.app",
    "localhost",
    "127.0.0.1",
]

# Agregar el dominio asignado por Vercel, si existe.
vercel_url = os.environ.get("VERCEL_URL", "").strip()

if vercel_url:
    vercel_url = vercel_url.removeprefix("https://").removeprefix("http://").rstrip("/")
    if vercel_url not in ALLOWED_HOSTS:
        ALLOWED_HOSTS.append(vercel_url)

# Orígenes autorizados para formularios POST y protección CSRF.
CSRF_TRUSTED_ORIGINS = [
    "https://solicitud1.vercel.app",
    "https://solicitud1-b5pnc4vmr-abkeno.vercel.app",
]

if vercel_url:
    origin = f"https://{vercel_url}"
    if origin not in CSRF_TRUSTED_ORIGINS:
        CSRF_TRUSTED_ORIGINS.append(origin)

# Permitir agregar más orígenes desde las variables de entorno.
extra_csrf_origins = os.environ.get("CSRF_TRUSTED_ORIGINS", "")

for origin in extra_csrf_origins.split(","):
    origin = origin.strip().rstrip("/")
    if origin and origin not in CSRF_TRUSTED_ORIGINS:
        CSRF_TRUSTED_ORIGINS.append(origin)


# Vercel termina HTTPS en su proxy.
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")


# ==========================================================
# APLICACIONES
# ==========================================================

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "incidencias",
]


# ==========================================================
# MIDDLEWARE
# ==========================================================

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


# ==========================================================
# URLS Y WSGI
# ==========================================================

ROOT_URLCONF = "config.urls"

WSGI_APPLICATION = "config.wsgi.application"


# ==========================================================
# PLANTILLAS HTML
# ==========================================================

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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


# ==========================================================
# BASE DE DATOS: NEON POSTGRESQL / SQLITE LOCAL
# ==========================================================

DATABASE_URL = (
    os.environ.get("DATABASE_URL")
    or os.environ.get("abkenosolicitud_DATABASE_URL")
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
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }


# ==========================================================
# VALIDACIÓN DE CONTRASEÑAS
# ==========================================================

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
            "NumericPasswordValidator"
        ),
    },
]


# ==========================================================
# IDIOMA Y ZONA HORARIA
# ==========================================================

LANGUAGE_CODE = "es-mx"

TIME_ZONE = "America/Mexico_City"

USE_I18N = True

USE_TZ = True


# ==========================================================
# ARCHIVOS ESTÁTICOS: CSS, JAVASCRIPT E IMÁGENES
# ==========================================================

STATIC_URL = "/static/"

STATIC_ROOT = BASE_DIR / "staticfiles"

# WhiteNoise sirve los archivos estáticos en producción.
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": (
            "whitenoise.storage.CompressedStaticFilesStorage"
        ),
    },
}


# ==========================================================
# AUTENTICACIÓN
# ==========================================================

LOGIN_URL = "/accounts/login/"

LOGIN_REDIRECT_URL = "/"

LOGOUT_REDIRECT_URL = "/accounts/login/"


# ==========================================================
# SESIONES Y COOKIES
# ==========================================================

SESSION_COOKIE_SECURE = not DEBUG

CSRF_COOKIE_SECURE = not DEBUG

SESSION_COOKIE_HTTPONLY = True

CSRF_COOKIE_HTTPONLY = False

SESSION_COOKIE_SAMESITE = "Lax"

CSRF_COOKIE_SAMESITE = "Lax"


# ==========================================================
# CONFIGURACIÓN GENERAL
# ==========================================================

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
