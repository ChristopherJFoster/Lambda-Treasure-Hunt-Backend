import os
import json


from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import get_object_or_404, render

from .models import Room
from .scripts import autohunt
from LTHBE.settings import BASE_DIR


def index(request):
    rooms_list = Room.objects.order_by('room_id')
    context = {'rooms_list': rooms_list, }
    return render(request, 'autohunt/index.html', context)

# def autohunt(request):
#     # runs autohunt script
#     return HttpResponse


def convert_map(request):

    map = {}
    PATH = os.path.join(BASE_DIR, 'mapDataFull.json')
    try:
        with open(PATH, 'r') as f:
            map = json.load(f)
    except FileNotFoundError:
        print(f'The file does not exist, no map loaded')

    for k, v in map.items():
        try:
            Room.objects.get(room_id=k)
        except:
            room_id = k
            coordX = int(v['coords'][1:-1].split(',')[0])
            coordY = int(v['coords'][1:-1].split(',')[1])
            exitN = v['exits'].get('n', 'X')
            exitE = v['exits'].get('e', 'X')
            exitS = v['exits'].get('s', 'X')
            exitW = v['exits'].get('w', 'X')
            Room.objects.create(room_id=room_id, coordX=coordX,  coordY=coordY,
                                exitN=exitN, exitE=exitE, exitS=exitS, exitW=exitW, )

    return JsonResponse({'message': 'You got the map! ...(or did you?)'})
