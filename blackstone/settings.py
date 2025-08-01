# settings.py

from pathlib import Path
import os
from dotenv import load_dotenv

# -----------------------------------------------------------------------------
# 1) Load .env (for local dev) and basic paths
# -----------------------------------------------------------------------------
load_dotenv()
BASE_DIR = Path(__file__).resolve().parent.parent

# -----------------------------------------------------------------------------
# 2) Core settings
# -----------------------------------------------------------------------------
SECRET_KEY = os.getenv("SECRET_KEY")
DEBUG = os.getenv("DEBUG", "false").lower() == "true"

# -----------------------------------------------------------------------------
# 3) ALLOWED_HOSTS: custom domains + this Vercel URL + all vercel.app
# -----------------------------------------------------------------------------
if DEBUG:
    ALLOWED_HOSTS = ["127.0.0.1", "localhost"]
else:
    ALLOWED_HOSTS = [
        # Your production domain(s) — no https://, no slash
        "profitnexusoptionhub.shop",
        "www.profitnexusoptionhub.shop",

        # Vercel production host
        "options-trades.vercel.app",

        # Catch any preview subdomain on vercel.app
        ".vercel.app",
    ]


# -----------------------------------------------------------------------------
# 4) Installed apps, middleware, URLs, templates, WSGI, etc.
# -----------------------------------------------------------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "app.apps.AppConfig",
    "auth_app.apps.AuthAppConfig",
    "user.apps.UserConfig",
    "user_admin.apps.UserAdminConfig",
    "users.apps.UsersConfig",
]

MIDDLEWARE = [
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

CORS_ALLOW_ALL_ORIGINS = True
ROOT_URLCONF = "blackstone.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "user_admin.context_processors.total_balance_admin",
                "user_admin.context_processors.unread_notification_count",
                "user.context_processors.total_balance_user",
                "user.context_processors.unread_notification_count",
            ],
        },
    },
]

WSGI_APPLICATION = "blackstone.wsgi.application"

# -----------------------------------------------------------------------------
# 5) Database (Neon Postgres)
# -----------------------------------------------------------------------------
DATABASES = {
    "default": {
        "ENGINE": os.getenv("DB_ENGINE", "django.db.backends.postgresql"),
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST", "localhost"),
        "PORT": os.getenv("DB_PORT", "5432"),
    }
}

# -----------------------------------------------------------------------------
# 6) Auth, i18n, static/media, default auto field
# -----------------------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True
AUTH_USER_MODEL = "users.User"

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# -----------------------------------------------------------------------------
# 7) Email settings
# -----------------------------------------------------------------------------
DEFAULT_EMAIL = os.getenv("DEFAULT_EMAIL")
if DEBUG:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
else:
    EMAIL_BACKEND = "app.utils.CertifiEmailBackend"
    EMAIL_HOST       = os.getenv("EMAIL_HOST", "smtp.gmail.com")
    EMAIL_PORT       = int(os.getenv("EMAIL_PORT", 587))
    EMAIL_USE_TLS    = os.getenv("EMAIL_USE_TLS", "true").lower() == "true"
    EMAIL_HOST_USER  = os.getenv("EMAIL_HOST_USER")
    EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")
