from django.urls import path

from . import views

app_name = 'autohunt'
urlpatterns = [
    # ex: /autohunt/
    path('', views.index, name='index'),
    # ex: /autohunt/convert-map
    path('convert-map', views.convert_map),
    # ex: /autohunt/traverse-treasure
    path('traverse-treasure', views.traverseTreasure),
    # ex: /autohunt/traverse-no-treasure
    path('traverse-no-treasure', views.traverseNoTreasure),
]
