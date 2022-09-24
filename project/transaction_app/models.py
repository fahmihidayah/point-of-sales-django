from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.


class Transaction(models.Model):
    invoice_number: models.CharField = models.CharField(max_length=255)

    total: models.FloatField = models.FloatField()

    user: models.ForeignKey = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)

    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)

    updated_at: models.DateTimeField = models.DateTimeField(auto_now=True)

    def __str__(self):
        return " " + str(self.invoice_number) + " " + str(self.total) + " " + str(
            self.user.pk) + " " + str(self.created_at) + " " + str(self.updated_at)
