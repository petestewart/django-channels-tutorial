from django.urls import path
from django.conf.urls import include

from rest_framework import routers

from . import views

# router = routers.DefaultRouter(trailing_slash=False)
# router.register(r'hello', views.hello, 'hello')

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
    # path('', include(router.urls), views.index, name='index')
]