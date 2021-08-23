import requests
from time import sleep
from base.models import Interaction
from django.shortcuts import get_object_or_404

TOKEN = '1976901283:AAHBO1sYlkhbylquFKDYUmo_n6RFTyO1IwM'

# FUNCIONANDO -----------------#
'''def send_message(text, chat_id):
    url = 'https://api.telegram.org/bot{}/sendMessage'.format(TOKEN)
    data = {'chat_id': chat_id, 'text': text}
    response = requests.post(url, data=data)
    print(response.content)'''
# FIM DE FUNCIONANDO --------------- #


def process_message(command):
    interaction = Interaction.objects.get(input=command)
    # interaction = get_object_or_404(Interaction, input=command)
    return interaction.output


def send_message(text, chat_id):
    url = 'https://api.telegram.org/bot{}/sendMessage'.format(TOKEN)
    data = {'chat_id': chat_id, 'text': text}
    response = requests.post(url, data=data)
    print(response.content)




# Testando um GET ----------
'''
def get_message(update_id):
    url = 'https://api.telegram.org/bot{0}/getUpdates?offset={1}'.format(TOKEN, update_id)
    response = requests.get(url)
    response_json = response.json()
    last_update_id = update_id
    for i in response_json['result']:
        first_name = i['message']['chat']['first_name']
        last_name = i['message']['chat']['last_name']
        chat_id = i['message']['chat']['id']
        last_update_id = i['update_id']
        text = i['message']['text']
        print(first_name, last_name, chat_id, update_id, text)
        if last_update_id != update_id:
            if "Chocolate" in text:
                send_message('Chocolate é do Mexico', chat_id)
            elif "Pimenta" in text:
                send_message('Habanero?', chat_id)
    return last_update_id


if __name__ == '__main__':
    # send_message()
    update_id = "467000927"
    while True:
        update_id = get_message(update_id)
        sleep(5)
'''
