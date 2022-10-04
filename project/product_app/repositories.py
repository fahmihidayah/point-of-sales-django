from .models import Product
from django.db.models import Q, Manager, QuerySet

class ProductRepository:

    def __init__(self):
        self.default_manager : Manager = Product.objects
        self.default_query_set : QuerySet = self.default_manager.all()

    def find_by_company(self, company) -> QuerySet:
        return self.default_query_set.filter(Q(company=company))

    def get_by_id(self, id) :
        try:
            return self.default_query_set.get(Q(pk=id))
        except:
            return None

    def save(self, data) -> Product:
        product : Product = self.default_manager.create(
            name=data['name'],
            description=data['description'],
            image=data['image'],
            price=data['price'],
            company=data['company'],
            stock=data['stock']
        )

        return product

