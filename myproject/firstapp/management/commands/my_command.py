from django.core.management.base import BaseCommand
from firstapp.models import Autor



class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        for i in range(1, 11):
            author = Autor(name=f'name {i}',
                           surname=f"surname {i}",
                           email=f"user {i}@mail.com",
                           biography="Моя биография ! ",
                           birthday=f"2000-01-{i}")
            author.save()