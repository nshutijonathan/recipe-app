from django.urls import path
from .views import home
app_name = 'ingredients'
path('', home, name='home')

urlpatterns = [
    path('', home),
]
