from datetime import timedelta
from pathlib import Path

from decouple import config
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Путь к файлу .env на один уровень выше папки server
dotenv_path = Path(BASE_DIR).parent.parent / ".env"

# Загружаем переменные окружения
load_dotenv(dotenv_path)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config("SECRET_KEY_AUTH")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "0.0.0.0"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "django.contrib.staticfiles",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.admin",
    "rest_framework",
    "auth_microservice_app",
    "drf_yasg",
    "corsheaders",
    # 'silk', # для профилирования
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    # 'silk.middleware.SilkyMiddleware', # для профилирования
]

CSRF_TRUSTED_ORIGINS = [
    "http://localhost",
    "http://localhost:3000",
    "https://localhost",
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost",
    "https://localhost",
    "http://localhost:3000",
]

CORS_ALLOW_CREDENTIALS = True  # Разрешить отправку с учётом CORS-заголовков
# Если фронтенд и бекенд на разных портах, разрешаем все источники (НЕ
# рекомендуется для продакшена)
CORS_ALLOW_ALL_ORIGINS = False  # False для безопасности в продакшене
CORS_ALLOW_METHODS = [
    "GET",
    "POST",
    "PUT",
    "PATCH",
    "DELETE",
    "OPTIONS",
]
CORS_ALLOW_HEADERS = [
    "Authorization",
    "Content-Type",
    "Set-Cookie",
    "X-CSRFToken",
    "X-Requested-With",
]

ROOT_URLCONF = "auth_microservice_core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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


WSGI_APPLICATION = "auth_microservice_core.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("DATABASE_NAME_AUTH"),
        "USER": config("DATABASE_USER_AUTH"),
        "PASSWORD": config("DATABASE_PASSWORD_AUTH"),
        "HOST": config("DATABASE_HOST_AUTH"),
        "PORT": config("DATABASE_PORT_AUTH"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
AUTH_USER_MODEL = "auth_microservice_app.CustomUser"


REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",  # Для открытых API
        # 'rest_framework.permissions.IsAuthenticated',
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}


SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=60),
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": True,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": config("JWT_SIGNING_KEY"),
}

# SILKY_PYTHON_PROFILER = True  # Включает профайлер
# SILKY_META = True  # Включает сбор дополнительной информации о запросах

MMEDIA_ROOT = "/uploads"
MEDIA_URL = "/uploads/"


EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = config("EMAIL_HOST_AUTH")
EMAIL_PORT = config("EMAIL_PORT_AUTH", cast=int)
EMAIL_USE_TLS = config("EMAIL_USE_TLS_AUTH", cast=bool)
EMAIL_HOST_USER = config("EMAIL_HOST_USER_AUTH")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD_AUTH")
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
