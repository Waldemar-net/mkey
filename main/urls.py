from django.urls import path
from main import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('agreement/', views.agreement, name='agreement'),
    path('privacy/', views.privacy, name='privacy'),
    path('support/', views.support, name="support"),
    path('support/send/', views.support_send, name="support-send"),
    path('send-support/', views.contact_view, name='contact'),
    path('404/', views.get_404, name='404'),
    path('admin-panel/', views.admin_panel, name='admin-panel'),
    path('admin-panel/game/add', views.admin_panel_game_add, name='game-add'),
    path('add-game/', views.add_game, name='add_game'),
    #новый index
    path('main/index', views.mains, name="mains"),
    #mobail-menu
    path('catalog/mob/menu', views.mob_menu_catalog, name='menu-mobail'),
]