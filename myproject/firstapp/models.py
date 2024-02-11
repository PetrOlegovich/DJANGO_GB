from django.db import models

'''
Задание №1

Создайте модель для запоминания бросков монеты: орёл или решка. 
Также запоминайте время броска.
'''
class Coin(models.Model):
   side = models.CharField(choices=(('орел', 'орел'),('решка', 'решка')), max_length=5)
   game_time = models.DateTimeField(auto_now_add=True)

   @staticmethod
   def count_trow():
      coin = Coin.objects.all()
      print(coin)
      dict_coin = {'Орёл': 0, 'Решка':0}

      for item in coin:
         if item.side == 'Орёл':
            dict_coin['Орёл'] +=1
         else:
            dict_coin['Решка'] +=1
      return dict_coin

   def __repr__(self):
      return f'{self.side}, {self.pk}'

   def __str__(self):
      return f'{self.side}, {self.pk}'


class Autor(models.Model):
   name = models.CharField(max_length=100)
   surname = models.CharField(max_length=100)
   email = models.EmailField()
   biography = models.TextField()
   birthday = models.DateField()


   def full_name(self):
      return f"{self.name} {self.surname}"


class Client(models.Model):
   name = models.CharField(max_length=100)
   email = models.EmailField()
   phone = models.CharField(max_length=20)
   address = models.TextField()
   time_create = models.DateField(auto_now_add=True)

   def __str__(self):
      return f'Name: {self.name},' \
             f' Email: {self.email},' \
             f' Phone: {self.phone},' \
             f' Address: {self.address}'


class Product(models.Model):
   name = models.CharField(max_length=150, verbose_name="Название")
   description = models.TextField(blank=True, verbose_name="Описание")
   price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
   amount = models.PositiveIntegerField(verbose_name="Количество")
   time_create = models.DateField(auto_now_add=True, verbose_name="Дата добавления")

   def __str__(self):
      return f'Name: {self.name},' \
             f' description: {self.description},' \
             f' price: {self.price},' \
             f' amount: {self.amount}'

   def get_full_description(self):
      return f'Name: {self.name},' \
             f' description: {self.description},' \
             f' price: {self.price},' \
             f' amount: {self.amount}'


class Order(models.Model):
   client = models.ForeignKey(Client, on_delete=models.CASCADE)
   products = models.ManyToManyField(Product)
   total_amount = models.DecimalField(max_digits=10, decimal_places=2)
   time_create = models.DateField(auto_now_add=True)

   def __str__(self):
      return f"Заказ от {self.client} на сумму {self.total_amount}"