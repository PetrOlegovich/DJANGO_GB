from django.core.management.base import BaseCommand
from firstapp.models import Product



class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for i in range(1, 11):
            author = Product (name=f'продукт под номером - {i}',
                           description=f"очень классный продукт под номером  {i}",
                           price=f"{i}.{i}",
                           amount=f"{i}",
                           time_create=f"1994-01-{i}")
            author.save()
