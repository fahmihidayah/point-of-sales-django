from django.db import models
from product_app.models import Product
from transaction_app.models import Transaction
from django.contrib.auth import get_user_model
from company_app.models import Company

# Create your models here.


class OrderItem(models.Model):

    product: models.ForeignKey = models.ForeignKey(to=Product, on_delete=models.CASCADE)

    amount: models.IntegerField = models.IntegerField()

    user: models.ForeignKey = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)

    company: models.ForeignKey = models.ForeignKey(to=Company, on_delete=models.CASCADE, default='')

    transaction: models.ForeignKey = models.ForeignKey(to=Transaction, default=None, null=True, on_delete=models.CASCADE)

    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)

    updated_at: models.DateTimeField = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.name + " - " + str(self.amount)

    class Meta:
        verbose_name_plural = "Order Items"