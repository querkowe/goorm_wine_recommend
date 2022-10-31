from django.urls import path
from . import views # 같은 폴더 내의 views.py를 import

app_name = 'recommand'

urlpatterns = [
    # "127.0.0.1:8000/recommand/" 이후의 URL은 search/urls.py가 handling하도록 만들 예정입니다.
    # path('', views.index, name='index'), # '127.0.0.1:8000/recommand/' 를 받아내도록 만들어줄 것입니다.
    # path('detail/', views.detail ,name='detail'),

    # "127.0.0.1:8000/recommand/" 이후의 URL은 search/urls.py가 handling하도록 만들 예정입니다.
    path('', views.main, name='index'),
    path('recommand/', views.index, name='search'), # '127.0.0.1:8000/recommand/' 를 받아내도록 만들어줄 것입니다.
    path('recommand/detail/', views.detail ,name='detail'),
    # path('autocomplete', views.autocomplete ,name='autocomplete'),
]
