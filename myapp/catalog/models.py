from django.db import models

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    date_of_birth = models.DateField()
    is_gold_customer = models.BooleanField()

    class Meta:
        managed = True