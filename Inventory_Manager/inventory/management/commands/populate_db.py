from django.core.management.base import BaseCommand
from inventory.models import Warehouse, Product, Stock, Supply, SuppliedProduct
from faker import Faker



class Command(BaseCommand):
    help = 'Populates the database with fake warehouse, product, and supply data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        if Product.objects.exists() or Warehouse.objects.exists():
            self.stdout.write(self.style.WARNING('Database already populated. Skipping.'))
            return

        warehouses = []
        for _ in range(10):
            warehouse = Warehouse.objects.create(
                name=f'Warehouse {fake.city()}',
                location=fake.address()
            )
            warehouses.append(warehouse)

        products = []
        for _ in range(10):
            product = Product.objects.create(
                name=f'{fake.word().capitalize()} {fake.word().capitalize()}',
                art=f'ART{fake.unique.random_number(digits=6)}',
                description=fake.text()
            )
            products.append(product)

        for warehouse in warehouses:
            for product in products:
                Stock.objects.create(
                    product=product,
                    warehouse=warehouse,
                    quantity=fake.random_int(min=0, max=100)
                )

        supplies = []
        for warehouse in warehouses:
            supply = Supply.objects.create(
                warehouse=warehouse,
                supplier_name=fake.company()
            )
            supplies.append(supply)

        for supply in supplies:
            for product in products:
                SuppliedProduct.objects.create(
                    supply=supply,
                    product=product,
                    quantity=fake.random_int(min=1, max=50)
                )

        self.stdout.write(self.style.SUCCESS('Database populated successfully!'))