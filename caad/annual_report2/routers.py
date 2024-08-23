# your_project/routers.py

class DatabaseRouter:
    """
    A router to control all database operations on models in the 'annual_report2' app.
    """
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'annual_report2':
            return 'annual_report_db'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'annual_report2':
            return 'annual_report_db'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'annual_report2' or obj2._meta.app_label == 'annual_report2':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'annual_report2':
            return db == 'annual_report_db'
        return db == 'default'
