from django.urls import path
from .views import Home, Link_Not_Found

app_name = 'Home'
urlpatterns = [
    path('', Home, name='Home'),
    path('NotFound/', Link_Not_Found, name='NotFound'),
    ]