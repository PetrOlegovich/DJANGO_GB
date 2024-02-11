
from django.urls import path
from .views import index, about
from django.urls import path


from . import views

urlpatterns = [

    path('', views.index, name='home'),
    path('game_1/', views.game_1, name='game_1'),
    path('game_2/', views.game_2, name='game_2'),
    path('game_3/', views.game_3, name='game_3'),
    path('about_me/', views.about_me, name='about_me'),
    path('static_game/', views.static_game, name='static_game'),
    path('full_name/', views.full_name, name='full_name'),
    path('about/', views.about, name='about'),
    path('author/<int:author_id>', views.show_posts, name='show_posts'),
    path('post/<int:post_id>', views.show_post_id, name='show_post_id'),
    path('user/<int:user_id>/', views.user_order, name='user_orders'),
    path('order/<int:order_id>/', views.order_full, name='order_full'),

]