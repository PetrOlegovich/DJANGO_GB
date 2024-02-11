from django.core.management.base import BaseCommand
from firstapp.models import Client




class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for i in range(1, 11):
            author = Client(name=f'Клиент {i}',
                            email=f"user {i}@gmail.com",
                            phone=f'{i+i}8{i}8{i}8{i}8{i}8{i}495',
                            address=f'Город {i}, улица {i}',
                            time_create=f"2000-01-{i}")
            author.save()


