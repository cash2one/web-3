# -*- coding: utf-8 -*-
import platform


SECRET_KEY = '6a8w1=^^n-sj0=n$%gsj@=kk%#bg(943vnt1_vq3@ylhofrp%^'
SESSION_SAVE_EVERY_REQUEST = False
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_COOKIE_AGE = 60 * 60 * 24 * 7 * 2
SESSION_COOKIE_DOMAIN = None
SESSION_COOKIE_NAME = "my_session_id"
SESSION_COOKIE_SECURE = False
SESSION_ENGINE = 'django.contrib.sessions.backends.db'
SESSION_FILE_PATH = None
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'


PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.UnsaltedSHA1PasswordHasher',
    'django.contrib.auth.hashers.UnsaltedMD5PasswordHasher',
    'django.contrib.auth.hashers.CryptPasswordHasher',
]
ALLOWED_HOSTS = ['*']


# 不允许访问的客户端————反爬虫
# DISALLOWED_USER_AGENTS = [
#     re.compile(r'^NaverBot.*'),
#     re.compile(r'^EmailSiphon.*'),
#     re.compile(r'^SiteSucker.*'),
#     re.compile(r'^sohu-search')
# ]
#
DEBUG = False
if platform.system() == "Windows":
    DEBUG = True


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
