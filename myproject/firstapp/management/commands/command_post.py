from random import randint, choice

from django.core.management.base import BaseCommand
from firstapp.models import Author, Posts



class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        authors = Author.objects.all()

        for author in authors:
            for i in range(randint(10, 15)):
                post = Posts(name_title= f'Post # {i + 1}',
                             description= "Some Text",
                             category= f'{choice(["документальная","историческая","политическая"])}',
                             count_watching= f'{randint(0,1000)}',
                             is_pablished=f'{choice([True, False])}',
                             author=author
                             )
                post.save()






            # name_title = models.CharField(max_length=200)
            # description = models.TextField()
            # date = models.DateField(auto_now_add=True)
            # author = models.ForeignKey(Autor, on_delete=models.CASCADE)
            # category = models.CharField(max_length=100)
            # count_watching = models.IntegerField(default=0)
            # is_pablished = models.BooleanField(default=False)