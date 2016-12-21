# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
import platform

host = '127.0.0.1'
if platform.system() == "Windows":
    host = "vm.test.com"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'manage',
        'USER': 'root',
        'PASSWORD': 'zdd12315',
        'HOST': host,
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}