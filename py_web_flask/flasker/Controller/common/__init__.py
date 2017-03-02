# coding=utf-8

from DataConnect.DataSource import corp_database, corp_database_read_1
def init(app):
    @app.teardown_request
    def _db_close(exc):
        if not corp_database.is_closed():
            corp_database.close()
        if not corp_database_read_1.is_closed():
            corp_database_read_1.close()