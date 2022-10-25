from tkinter import W
from django.urls import path
from . import views # 같은 폴더 내의 views.py를 import 
# from .views import add_wine_data 

app_name = 'main'

urlpatterns = [
    # "127.0.0.1:8000/main/" 이후의 URL은 main/urls.py가 handling하도록 만들 예정입니다.
    path('', views.index, name='index'), # '127.0.0.1:8000/main/' 를 받아내도록 만들어줄 것입니다. 
    # path('winedt/', add_wine_data)
]