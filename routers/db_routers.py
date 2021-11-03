class AuthRouter:
    route_app_labels={'auth','contenttypes','sessions','admin'}

    def db_for_read(self,model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'dcs_db'

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
                return 'dcs_db'

    def allow_relation(self, obj1, obj2, **hints):
        if(
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None,**hints):
        if app_label in self.route_app_labels:
            return 'dcs_db'
        return None

class NodeRouter:
    route_app_labels={'SCADA'}

    def db_for_read(self,model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'local_db'

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
                return 'local_db'

    def allow_relation(self, obj1, obj2, **hints):
        if(
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None,**hints):
        if app_label in self.route_app_labels:
            return 'local_db'
        return None