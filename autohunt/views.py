import os
import json


from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import get_object_or_404, render

from .models import Room
from LTHBE.settings import BASE_DIR

from .traverse import initialize as loot
from .traverseFullLoopNoTreasure import command_loop as traverseWithoutTreasure


def index(request):
    rooms_list = Room.objects.order_by('room_id')
    context = {'rooms_list': rooms_list, }
    return render(request, 'autohunt/index.html', context)


def lambda_loot(request, key):
    print('KEYKEYKEY: ', key)
    loot(key)
    return JsonResponse({'message': 'Auto-traversing...'})


def traverseNoTreasure(request):
    traverseWithoutTreasure('auto')
    return JsonResponse({'message': 'Auto-traversing...'})


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
