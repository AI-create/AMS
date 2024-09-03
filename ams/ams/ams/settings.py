from pathlib import Path
import os
import environ

# Initialize environment variables
env = environ.Env()
environ.Env.read_env()

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY', default='django-insecure-t3*r8lllbad(bkorc^e_9a^l0+%7oa=#(9y)15ec6osq^5yry4')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG', default=False)

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '3.27.120.1', 'd2xtaexzsbvmol.cloudfront.net', '172.31.0.236', 'alb-78546039.ap-southeast-2.elb.amazonaws.com', '54.252.200.211']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',  # Required for allauth
    'django_extensions',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'articles',
    'rest_framework',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

CSRF_TRUSTED_ORIGINS = [
    'https://d2xtaexzsbvmol.cloudfront.net',  # Add your CloudFront URL here
    # You can add other domains if needed
]

CSRF_COOKIE_SECURE = True  # Ensure CSRF cookies are only sent over HTTPS


ROOT_URLCONF = 'ams.urls'

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

WSGI_APPLICATION = 'ams.wsgi.application'

# Database Configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DB_NAME', default='myamsdb'),
        'USER': env('DB_USER', default='postgres'),
        'PASSWORD': env('DB_PASSWORD', default='N98l4TeCdArWhNPIBVbq'),
        'HOST': env('DB_HOST', default='database-1.ct4mm4im061z.ap-southeast-2.rds.amazonaws.com'),
        'PORT': env('DB_PORT', default='5432'),
    }
}

# AWS S3 Settings for file storage
AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Django Allauth configuration
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

SITE_ID = 1

# # Allauth settings
# ACCOUNT_EMAIL_VERIFICATION = 'none'
# ACCOUNT_AUTHENTICATION_METHOD = 'email'
# ACCOUNT_EMAIL_REQUIRED = True

# Social account providers
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': env('SOCIAL_GOOGLE_CLIENT_ID'),
            'secret': env('SOCIAL_GOOGLE_CLIENT_SECRET'),
            'key': ''
        },
        'AUTH_PARAMS': {
            'access_type': 'offline',
        },
        'OAUTH2_CLIENT_ID': env('SOCIAL_GOOGLE_CLIENT_ID'),
        'OAUTH2_CLIENT_SECRET': env('SOCIAL_GOOGLE_CLIENT_SECRET'),
        'OAUTH2_STATIC_REDIRECT_URI': 'http://d2xtaexzsbvmol.cloudfront.net/accounts/google/login/callback/',
    }
}





# CORS configuration
CORS_ALLOW_ALL_ORIGINS = True

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
