from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('profile/', views.profile, name='profile'),
    path('profile/data/', views.data, name='data'),
    path('logout/', views.logout, name='logout'),
    path('profile/cart', views.users_cart, name="users-cart"),
    path('profile/my-oreders', views.my_orders, name='my-orders'),
    path('password-reset/', views.password_reset, name='password_reset'),
    path('game/add-product/', views.add_product, name='add-product'),
    path('game/add-new-game/', views.add_new_game, name='add-new-game'),
]
 