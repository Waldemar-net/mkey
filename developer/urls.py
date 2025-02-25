from django.urls import path
from developer import views

app_name = 'developer'

urlpatterns = [
    path('',views.developers, name="developers"),
    path('<slug:developer_name_slug>/', views.developer, name="developer"),
    
    
]
 