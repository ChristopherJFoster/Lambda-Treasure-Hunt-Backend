from django.urls import path

from . import views

app_name = 'autohunt'
urlpatterns = [
    # ex: /autohunt/
    path('', views.index, name='index'),
    # ex: /autohunt/convert-map
    path('convert-map', views.convert_map),
    # ex: /autohunt/traverse
    path('traverse', views.traverse),
]
