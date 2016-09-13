# coding=utf-8
import datetime

from flask.ext.session import Session
import memcache, appconfig


SESSION_TYPE = 'memory'
SESSION_COOKIE_NAME = appconfig.SESSION_COOKIE_NAME
SESSION_COOKIE_DOMAIN = ''

PERMANENT_SESSION_LIFETIME = datetime.timedelta(hours=8)


SESSION_MEMCACHED = memcache.Client([appconfig.MEMCACHE_URL])


def init(app):
    app.config.from_object(__name__)
    Session(app)
