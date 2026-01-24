import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

# Carrega o arquivo .env que está na raiz
load_dotenv(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'chave-temporaria-se-o-env-falhar')
DEBUG = os.getenv('DJANGO_DEBUG', 'False') == 'True'

ALLOWED_HOSTS = ['multiplacreditos7.pythonanywhere.com', 'localhost', '127.0.0.1']

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'register_lead',
]

JAZZMIN_SETTINGS = {
    "site_title": "Múltipla Créditos Admin",
    "site_header": "Múltipla Créditos",
    "site_brand": "Múltipla Créditos",
    "welcome_sign": "Bem-vindo ao Gestor de Leads",
    "copyright": "Múltipla Créditos © 2026",
    "search_model": ["register_lead.RegisterLead"],
    "icons": {
        "auth": "fas fa-users-cog",
        "register_lead.RegisterLead": "fas fa-address-card",
        "register_lead.Service": "fas fa-hand-holding-usd",
    },
    "show_sidebar": True,
    "navigation_expanded": True,
    "user_menu_open": True, 
    "logout_link": "admin:logout",
    "site_logo": "images/logo.png",  # Caminho relativo dentro da pasta static
    "login_logo": "images/logo.png", # Se quiser que apareça na tela de login também
    "site_icon": "images/logo.png",  # Favicon (ícone da aba do navegador)
    "custom_css": "css/admin_custom.css",
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Capture_lead.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Capture_lead.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_DIRS = [ BASE_DIR / 'static', ]