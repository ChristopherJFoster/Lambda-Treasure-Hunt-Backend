from django.urls import path

from . import views

app_name = 'autohunt'
urlpatterns = [
    # ex: /autohunt/
    path('', views.index, name='index'),
    # ex: /autohunt/convert-map
    path('convert-map', views.convert_map),

    # ex: /autohunt/loot/<API_KEY here>/
    path('loot/<str:key>/', views.lambda_loot),

    # path('loot/', views.lambda_loot),

    # ex: /autohunt/traverse-no-treasure
    path('traverse-no-treasure', views.traverseNoTreasure),
]
