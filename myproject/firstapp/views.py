from random import choice, randint
from django.http import HttpResponse
from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)

def index(request):
    logger.info('ты на главной странице! ')
    return render(request, 'firstapp/second.html')

def game_1(request):
    answer = choice(['Орёл', 'Решка'])
    logger.info(f'Ответ game_1   равен : {answer}')
    return HttpResponse(answer)

def game_2(request):
    answer = randint(1, 6)
    logger.info(f' game_2   равен : {answer}')
    return HttpResponse(answer)


def game_3(request):
    answer = randint(0, 100)
    logger.info(f'Ответ game_3   равен : {answer}')
    return HttpResponse(answer)

def about_me(request):
    logger.info('ты читаешь текст про меня')
    return render(request, 'firstapp/index.html')

