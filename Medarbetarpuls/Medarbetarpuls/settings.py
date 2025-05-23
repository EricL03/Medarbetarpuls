"""
Django settings for Medarbetarpuls project.

Generated by 'django-admin startproject' using Django 5.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-!q2_ak4#xg9w)0mz67&y3+bc0$g@l0ljbzyq)z76a)_^%66w()"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1"]

# Add ngrok host if the proxy is used...
ngrok_host = os.getenv("NGROK_HOST")
if ngrok_host:
    ALLOWED_HOSTS.append(ngrok_host)

# Add ngrok to CSRF trusted origins
if ngrok_host:
    CSRF_TRUSTED_ORIGINS = [f"https://{ngrok_host}"]
else:
    CSRF_TRUSTED_ORIGINS = []

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/
STATIC_URL = "/static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "medarbetarapp", "static"),
]

# Add static root for debug = False
# Run: python manage.py collectstatic, to collect static files
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "medarbetarapp", "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "medarbetarapp",
]

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

# Compressed static files...
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

ROOT_URLCONF = "Medarbetarpuls.urls"

WSGI_APPLICATION = "Medarbetarpuls.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {message}",
            "style": "{",
        },
        "simple": {
            "format": "{levelname} {message}",
            "style": "{",
        },
        "json": {  # For structured logs (optional)
            "()": "pythonjsonlogger.jsonlogger.JsonFormatter",
            "format": '{"time": "%(asctime)s", "level": "%(levelname)s", "module": "%(module)s", "message": "%(message)s"}',
            "style": "%",
        },
    },
    "handlers": {
        "file": {
            "level": "WARNING",
            "class": "logging.FileHandler",
            "filename": "logs/calc_debug.log",
            "formatter": "verbose",
        },
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
        "json_file": {  # JSON logs (optional)
            "level": "INFO",
            "class": "logging.FileHandler",
            "filename": "logs/calc_logs.json",
            "formatter": "json",
        },
    },
    "root": {
        "handlers": [
            "file",
            "json_file",
            "console",
        ],
        "level": "INFO",
    },
    "loggers": {
        "django": {
            "handlers": ["file", "console", "json_file"],
            "level": "INFO",
            "propagate": False,
        },
        "django.db.backends": {  # Logs SQL queries (useful for debugging slow queries)
            "handlers": ["file"],
            "level": "INFO",
            "propagate": False,
        },
    },
}


# Replaces Djangos built-in user with our custom one
AUTH_USER_MODEL = "medarbetarapp.CustomUser"

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

USE_TZ = True
TIME_ZONE = "Europe/Stockholm"
CELERY_TIMEZONE = "Europe/Stockholm"

USE_I18N = True


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"  # Gmail's SMTP server
EMAIL_PORT = 587  # TLS port
EMAIL_USE_TLS = True  # Use TLS encryption

EMAIL_HOST_USER = 'medarbetarpuls@gmail.com'  # Medarbetarpuls gmail
EMAIL_HOST_PASSWORD = 'oejv vxry kwrn ezoe'   # App password for gmail

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# Celery settings/setup for async task scheduling
CELERY_BROKER_URL = "redis://localhost:6379/0"
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"

SESSION_EXPIRE_AT_BROWSER_CLOSE = True  # Flush session when window is closed

