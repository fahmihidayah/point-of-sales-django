from . models import Category
from django.db.models import Manager, QuerySet, Q

class CategoryRepository :

    def __init__(self):
        self.manager : Manager = Category.objects
        self.default_query = self.manager.all()


    def find_all(self) -> QuerySet:
        return self.default_query

    def find_by_company(self, company) -> QuerySet:
        return self.default_query.filter(Q(company=company))

    def get_by_name(self, name):
        try:
            return self.default_query.get(Q(name=name))
        except:
            return None
