


from http.cookiejar import DefaultCookiePolicy
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

from dotenv import load_dotenv, find_dotenv

env_file = Path(find_dotenv(usecwd=True))
load_dotenv(verbose=True, dotenv_path=env_file)




# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-ehplvglk2g+u4588%foij-@6dtv^#jzqj*a#z9^1=$c249!9sa'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# if __name__ == "__main__":
#     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")


AUTH_USER_MODEL = "User.Profile"

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'drf_yasg',
  
    'User',
    'Cart',
    'Comment',
    'Product',
    'Notify',
    'Payment',
    'azbankgateways',
    'django_user_agents',
    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',
    'django_celery_results',
    
    'django_filters',


    'social_django', 
]



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #other MIDDLEWARE
    'django_user_agents.middleware.UserAgentMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',

]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/"templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'Product.context.header',

                'social_django.context_processors.backends',  
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }



SESSION_ENGINE = 'Cart.session_backend'

USER_AGENTS_CACHE = 'default'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get("DB_NAME", ""),
        'USER': os.environ.get("DB_USER", ""),
        'PASSWORD': os.environ.get("DB_PASSWORD", ""),
        'HOST': os.environ.get("DB_HOST", ""),
        'PORT': os.environ.get("DB_PORT", "5432"),
    }
}





# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
# STATICFILES_DIRS=[BASE_DIR/"static"]
MEDIA_URL="/media/"
MEDIA_ROOT=BASE_DIR/"media/"
CART_SESSION_ID='cart'

STATIC_ROOT = os.path.join(BASE_DIR, "static/")

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER =os.environ.get("EMAIL_HOST_USER","")
EMAIL_HOST_PASSWORD =os.environ.get("EMAIL_HOST_PASSWORD","")



AZ_IRANIAN_BANK_GATEWAYS = {
   'GATEWAYS': {
      
       'IDPAY': {
           'MERCHANT_CODE': os.environ.get("MERCHANT_CODE",""),
           'METHOD': 'POST',  # GET or POST
           'X_SANDBOX': 1,  # 0 disable, 1 active
       }

   },
   'IS_SAMPLE_FORM_ENABLE': True, # اختیاری و پیش فرض غیر فعال است
   'DEFAULT': 'IDPAY',
   'CURRENCY': 'IRR', # اختیاری
   'TRACKING_CODE_QUERY_PARAM': 'tc', # اختیاری
   'TRACKING_CODE_LENGTH': 16, # اختیاری
   'SETTING_VALUE_READER_CLASS': 'azbankgateways.readers.DefaultReader', # اختیاری
   'BANK_PRIORITIES': [
       # and so on ...
   ], # اختیاری
}

MY_USER_TOKEN_VALIDATION_DAY = 2


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework.authentication.TokenAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
# 'DEFAULT_PERMISSION_CLASSES': [
#     'rest_framework.permissions.IsAuthenticated',
# ]
}



AUTHENTICATION_BACKENDS = (
    
    'social_core.backends.github.GithubOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_GITHUB_KEY = '7f218aebcdd6b15f20a1'
SOCIAL_AUTH_GITHUB_SECRET = 'a9fc85a106f588d342ef02f09e45f90c1b511894'


# LOGIN_URL = '/'
# LOGOUT_URL = '/'
LOGIN_REDIRECT_URL = 'home'
# SOCIAL_AUTH_GITHUB_SCOPE = []

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.social_user',
    # 'social_core.pipeline.social_auth.social_details',
    # 'social_core.pipeline.user.get_username',
    # 'social_core.pipeline.social_auth.associate_by_email',
    # 'social_core.pipeline.user.create_user',
    # 'social_core.pipeline.social_auth.associate_user',
    # 'social_core.pipeline.social_auth.load_extra_data',
    # 'social_core.pipeline.user.user_details',
)

if DEBUG :
    from .setting_develope import *
    
else :
    from .setting_deploy import *