from django.urls import path
from publisher import views

app_name = 'publisher'

urlpatterns = [
    path('',views.publishers, name="publishers"),
    path('<slug:publisher_name_slug>/', views.publisher, name="publisher"),
    
    
]
 