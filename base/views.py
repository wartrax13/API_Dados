import json

from django.shortcuts import render
from django.http import JsonResponse
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from base.utils import send_message

@csrf_exempt
def event(requests):
    print(requests)
    json_list = json.loads(requests.body)
    print(json_list)
    chat_id = json_list['message']['chat']['id']
    send_message('Estou ocupado. Depois respondo.',chat_id)
    return HttpResponse()
    # return JsonResponse({'status': 'true', 'message':'worked'})
