from .base import *
import os



DEBUG = False

ALLOWED_HOSTS = ['localhost','aavgoustinos.pythonanywhere.com']

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


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'aavgoustinos$apac',
        'USER': 'aavgoustinos',
        'PASSWORD': 'bufallo-1',
        'HOST': 'aavgoustinos.mysql.pythonanywhere-services.com',
    }
}


STATIC_URL = 'static/'
STATIC_ROOT= os.path.join(BASE_DIR,'static')

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



