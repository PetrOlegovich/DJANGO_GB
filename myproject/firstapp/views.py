from random import choice, randint
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import render, get_object_or_404
import logging
from .models import Coin, Author, Posts, User, Product, Orders


logger = logging.getLogger(__name__)

def index(request):
    logger.info('ты на главной странице! ')
    return render(request, 'firstapp/index.html')

def about(request):
    logger.info('ты на главной странице! ')
    return render(request, 'firstapp/about.html')



def game_1(request):
    answer = choice(['Орёл', 'Решка'])
    coin = Coin(side=answer)
    coin.save()
    logger.info(f'Ответ game_1   равен : {answer}')
    context = {'result': answer}
    return render(request, 'firstapp/games.html', context)

def static_game(request):
    count = Coin.count_trow()
    return HttpResponse(f'Орёл : {count["Орёл"]}, Решка : {count["Решка"]}  ')



def game_2(request):
    answer = randint(1, 6)
    logger.info(f' game_2   равен : {answer}')
    context = {'result': answer}
    return render(request, 'firstapp/games.html', context)


def game_3(request):
    answer = randint(0, 100)
    logger.info(f'Ответ game_3   равен : {answer}')
    context = {'result': answer}
    return render(request, 'firstapp/games.html', context)

def about_me(request):
    logger.info('ты читаешь текст про меня')
    return render(request, 'firstapp/index.html')

def full_name(request):
    full_name = Autor.objects.all()
    result = ''
    for item in full_name:
        result += f'{item.full_name()}<br>'

    return HttpResponse(result)



def show_posts(request, author_id):
    author = Author.objects.get(pk=author_id)
    posts = Posts.objects.filter(author=author)

    context = {"posts": posts}
    return render(request, 'firstapp/posts.html', context)


def show_post_id(request, post_id):
    post = Posts.objects.get(pk=post_id)
    context = {"post": post}
    return render(request, 'firstapp/post.html', context)

def user_order(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    orders = Orders.objects.filter(customer=user).order_by('date_ordered')
    return render(request, 'firstapp/user_order.html', {'user': user, 'orders': orders})

def order_full(request, order_id):
    order = get_object_or_404(Orders, pk=order_id)
    return render(request, 'firstapp/order_full.html', {'order': order})
