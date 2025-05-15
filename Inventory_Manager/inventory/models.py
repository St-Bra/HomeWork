from django.db import models

class Warehouse(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} ({self.location})"

class Product(models.Model):
    name = models.CharField(max_length=255)
    art = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} (ATR: {self.art})"

class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('product', 'warehouse')

    def __str__(self):
        return f"{self.product.name} at {self.warehouse.name}: {self.quantity}"

class Supply(models.Model):
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    supplier_name = models.CharField(max_length=255)

    def __str__(self):
        return f"Supply to {self.warehouse.name} on {self.date.date()}"

class SuppliedProduct(models.Model):
    supply = models.ForeignKey(Supply, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity}x {self.product.name} (Supply ID: {self.supply.id})"