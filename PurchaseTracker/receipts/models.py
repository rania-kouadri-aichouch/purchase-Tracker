from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.utils import timezone


class Receipt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=255,blank=False, null=False)
    date_of_purchase = models.DateField(blank=False, null=False)
    item_list = models.TextField(blank=False, null=False)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2 ,validators=[MinValueValidator(0)] ,blank=False, null=False)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(default=timezone.now)    

    class Meta:
        verbose_name_plural = "Receipts"

    def __str__(self):
        return f"{self.store_name} - {self.date_of_purchase}"

