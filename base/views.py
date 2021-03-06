# from django.shortcuts import render
# from django.http import JsonResponse
from django.contrib.sites import requests

from base.utils import send_message, process_message
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json


@csrf_exempt
def event(requests):
    print(requests)
    json_list = json.loads(requests.body)
    print(json_list)
    chat_id = json_list['message']['chat']['id']
    command = json_list['message']['text']
    output = process_message(command)
    send_message(output, chat_id)
    return HttpResponse()
