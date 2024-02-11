from random import randint, choice

from django.core.management.base import BaseCommand
from firstapp.models import Order, Client



class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        clients = Client.objects.all()


        for client in clients:
            for i in range(1,5):

                order = Order(client=client,
                               product=f'{choice(["продукт номЕр один", "красная цена", "продукт три",])}',
                               total_amount=f"{i}.{i}",
                               time_create=f"2000-01-{i}")
                order.save()

