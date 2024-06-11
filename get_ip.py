from pprint import pprint
import socket
# mostra o id do último grupo adicionado
import requests
from time import sleep
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print(s.getsockname()[0])
ip = s.getsockname()[0]
ip2 = socket.gethostbyname(socket.gethostname())
print(socket.gethostbyname(socket.gethostname()))


def last_chat_id(token):
    try:
        url = "https://api.telegram.org/bot{}/getUpdates".format(token)
        response = requests.get(url)
        pprint(requests)
        if response.status_code == 200:
            json_msg = response.json()
            pprint(json_msg)

            for json_result in reversed(json_msg['result']):
                pprint(json_result)
                message_keys = json_result['my_chat_member'].keys()
                if ('new_chat_member' in message_keys) or ('group_chat_created' in message_keys):
                    return json_result['my_chat_member']['chat']['id']
            print('Nenhum grupo encontrado')
        else:
            print('A resposta falhou, código de status: {}'.format(
                response.status_code))
    except Exception as e:
        print("Erro no getUpdates:", e)

# enviar mensagens utilizando o bot para um chat específico


def send_message(token, chat_id, message):
    try:
        data = {"chat_id": chat_id, "text": message}
        url = "https://api.telegram.org/bot{}/sendMessage".format(token)
        requests.post(url, data)
    except Exception as e:
        print("Erro no sendMessage:", e)


token = 'tokentoken'

# id do chat que será enviado as mensagens
while True:
    try:
        chat_id = -000000  # last_chat_id(token)
        msg = f"IP:{ip} \n IP2:{ip2}"
        send_message(token, chat_id, msg)
        sleep(2)
    except Exception as e:
        print(f'Erro: {e}')
        sleep(1)
