import os
import json
from pathlib import Path

# 📁 Base Directory
BASE_DIR = Path(__file__).resolve().parent.parent

# 🔐 Security
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-...')
DEBUG = os.environ.get('DJANGO_DEBUG', 'True') == 'True'

# 🌍 Hosts and CSRF for Azure-(Correct for minimize-403 Forbidden Error)
try:
    ALLOWED_HOSTS = json.loads(os.environ.get(
        'DJANGO_ALLOWED_HOSTS',
        '["perp-ac-app.azurewebsites.net"]'
    ))
except (json.JSONDecodeError, TypeError):
    ALLOWED_HOSTS = ["perp-ac-app.azurewebsites.net"]

try:
    CSRF_TRUSTED_ORIGINS = json.loads(os.environ.get(
        'CSRF_TRUSTED_ORIGINS',
        '["https://perp-ac-app.azurewebsites.net", " https://perp-ac-app.azurewebsites.net"]'
    ))
except (json.JSONDecodeError, TypeError):
    CSRF_TRUSTED_ORIGINS = [
        " https://perp-ac-app.azurewebsites.net",
        " https://perp-ac-app.azurewebsites.net"
    ]

# 🔐 CSRF and Cookie Security for Azure
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = False

# ⚠️ Prevent redirect loops: Let Azure handle HTTPS
SECURE_SSL_REDIRECT = False

# ✅ Optional: Enable HSTS headers only in production
SECURE_HSTS_SECONDS = 3600 if not DEBUG else 0
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# 📦 Installed Apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Custom Apps
    'home',
    'construction',
    'design',
    'project',
    'client',
    'accounts',
]

# 🧱 Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'accounts.middleware.EnsureProfileAndDepartmentMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 🔐 Azure AD Department Mapping
DEPARTMENT_EMAIL_MAP = {
    'abir@dzignscapeprofessionals.onmicrosoft.com': 'construction',
    'bokul@dzignscapeprofessionals.onmicrosoft.com': 'design',
}

# 🔐 Azure AD Login Redirect
LOGIN_URL = '/.auth/login/aad'

# 🌐 URL & WSGI
ROOT_URLCONF = 'erp_project.urls'
WSGI_APPLICATION = 'erp_project.wsgi.application'

# 🧠 Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# 🗄️ Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DATABASE_NAME'),
        'USER': os.environ.get('DATABASE_USER'),
        'PASSWORD': os.environ.get('DATABASE_PASSWORD'),
        'HOST': os.environ.get('DATABASE_HOST'),
        'PORT': '5432',
        'OPTIONS': {
            'sslmode': 'require',
        },
    }
}

# 🔐 Password Validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# 🌍 Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Dhaka'
USE_I18N = True
USE_TZ = True

# 📦 Static Files
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "construction" / "static",
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

# 🆔 Default Primary Key
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'















