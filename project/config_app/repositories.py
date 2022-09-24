from . import models
from django.db.models import Manager, QuerySet, Q

class ConfigRepository:

    def __init__(self):
        self.manager : Manager = models.Config.objects
        self.default_query_set: QuerySet = self.manager.all()

    def find_all(self) -> QuerySet:
        return self.default_query_set.all()

    def get_by_id(self, id):
        try:
            return self.default_query_set.get(Q(pk=id))
        except:
            return None
