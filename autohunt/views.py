from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render

from .models import Room


def index(request):
    rooms_list = Room.objects.order_by('room_id')
    context = {'rooms_list': rooms_list, }
    return render(request, 'autohunt/index.html', context)
