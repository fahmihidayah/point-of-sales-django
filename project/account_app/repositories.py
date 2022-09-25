from .models import UserModel, models

class UserRepository:

    def __init__(self):
        self.manager = UserModel.objects
        self.default_query_set = self.manager.select_related('profile').prefetch_related('company_set')

    def find_by_id(self, id):
        return self.default_query_set.get(
            models.Q(pk=id)
        )
