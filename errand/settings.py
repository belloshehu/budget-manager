"""
Django settings for errand project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
from configurations import Configuration, values

class Dev(Configuration):
    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = '09onf5dn3qp+r6urhm^q*k1*+c8%+zmq&1%7!+nm48adx$mq)w'

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = values.BooleanValue(True)

    ALLOWED_HOSTS = values.ListValue(['*'])


    # Application definition

    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'custom_account',
    'item',
    'sharing',
    'reviews',
    'friendship',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.facebook',
    ]

    MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    ROOT_URLCONF = 'errand.urls'

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

    WSGI_APPLICATION = 'errand.wsgi.application'


    # Database
    # https://docs.djangoproject.com/en/2.2/ref/settings/#databases

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
    DATABASES = values.DatabaseURLValue(f"sqlite:///{BASE_DIR}/db.sqlite3")

    # Password validation
    # https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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

    PASSWORD_HASHERS = [
        'django.contrib.auth.hashers.Argon2PasswordHasher',
        'django.contrib.auth.hashers.PBKDF2PasswordHasher',
        'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
        'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    ]

    # Internationalization
    # https://docs.djangoproject.com/en/2.2/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = values.Value('UTC')

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True


    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/2.2/howto/static-files/

    AUTHENTICATION_BACKENDS = (
        "django.contrib.auth.backends.ModelBackend",
        "allauth.account.auth_backends.AuthenticationBackend",
    )

    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

    LOGIN_REDIRECT_URL = 'custom_account:dashboard'
    ACCOUNT_LOGOUT_REDIRECT_URL = 'account_login'
    ACCOUNT_AUTHENTICATED_LOGIN_REDIRECTS =True

    AUTH_USER_MODEL = 'custom_account.User'
    ACCOUNT_USERNAME_REQUIRED = True
    ACCOUNT_EMAIL_REQUIRED = True
    ACCOUNT_AUTHENTICATION_METHOD = 'email'
    ACCOUNT_EMAIL_VERIFICATION = False

    #Account Email:
    ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3
    ACCOUNT_EMAIL_VERIFICATION = "mandatory"
    ACCOUNT_EMAIL_SUBJECT_PREFIX  = "Budget Manager"

    # Account Login
    ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5
    ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
    SITE_NAME = 'Errand'
    SITE_ID = 1

    # Email config:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    EMAIL_HOST_USER = "belloshehu1@gmail.com"
    EMAIL_HOST_PASSWORD = "vrzjtkgkfpmpyxws"

    
    # client_id = 59307545249-3aoosvce98t12kjnan7iv98mkqn23g10.apps.googleusercontent.com
    # client_secret = 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

    SOCIALACCOUNT_PROVIDERS = {
        "github": {
            # For each provider, you can choose whether or not the
            # email address(es) retrieved from the provider are to be
            # interpreted as verified.
            "VERIFIED_EMAIL": False,
            'SCOPE': [
                'user',
            ],
        },
        "google": {
            # For each OAuth based provider, either add a ``SocialApp``
            # (``socialaccount`` app) containing the required client
            # credentials, or list them here:
            # These are provider-specific settings that can only be
            # listed here:
            "SCOPE": [
                "profile",
                "email",
            ],
            "AUTH_PARAMS": {
                "access_type": "online",
            }
        },
        'facebook': {
            'METHOD': 'oauth2',
            # 'SDK_URL': '//connect.facebook.net/{locale}/sdk.js',
            'SCOPE': ['email', 'public_profile'],
            'AUTH_PARAMS': {'auth_type': 'reauthenticate'},
            'INIT_PARAMS': {'cookie': True},
            'FIELDS': [
                'id',
                'first_name',
                'last_name',
                'middle_name',
                'name',
                'name_format',
                'picture',
                'short_name'
            ],
            'EXCHANGE_TOKEN': True,
            # 'LOCALE_FUNC': 'path.to.callable',
            'VERIFIED_EMAIL': False,
            'VERSION': 'v13.0',
        }
    }


class Prod(Dev):
    """
    Configuration for production.
    """
    DEBUG = values.BooleanValue(False)
    SECRET_KEY = values.SecretValue()