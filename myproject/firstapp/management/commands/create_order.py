from django.core.management.base import BaseCommand
from firstapp.models import Order



class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for i in range(1, 11):
            author = Order(client.id=f'{i}',
                           product=f"продукт {i}",
                           total_amount=f"{i}.{i}",
                           time_create=f"2000-01-{i}")
            author.save()

# ''' я так и не понял что да как тут сделать ((((
# '''