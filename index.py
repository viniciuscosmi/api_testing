import json
import requests

API_URL = 'http://localhost:3000/usuarios'

with open('payload/body.json', 'r') as file:
  body = json.load(file)

def send_request():
    response = requests.post(API_URL, json=body)
    save_log(response)
    
def save_log(value):
    file_name = 'log.txt'
    f = open(file_name, 'a+')
    f.write(f'Payload: {str(body)}')
    f.write('\n')
    f.write(f'Response: {str(value.json())}')
    f.write('\n')
    f.write(f'Status code: {str(value.status_code)}')
    f.write('\n\n')
    f.close()

def change_values_from_body_to_none(body):
    for k, v in body.items():
        if isinstance(v, dict):
            change_values_from_body_to_none(v)
        else:
            initial_value = body[k]
            body[k] = None
            send_request()
            body[k] = initial_value

def change_values_from_body_to_empty(body):
    for k, v in body.items():
        if isinstance(v, dict):
            change_values_from_body_to_empty(v)
        else:
            initial_value = body[k]
            body[k] = ''
            send_request()
            body[k] = initial_value

def change_values_from_body_to_int(body):
    for k, v in body.items():
        if isinstance(v, dict):
            change_values_from_body_to_int(v)
        else:
            initial_value = body[k]
            body[k] = 1
            send_request()
            body[k] = initial_value

def change_values_from_body_to_bool(body):
    for k, v in body.items():
        if isinstance(v, dict):
            change_values_from_body_to_bool(v)
        else:
            initial_value = body[k]
            body[k] = True
            send_request()
            body[k] = initial_value



change_values_from_body_to_none(body)
change_values_from_body_to_empty(body)
change_values_from_body_to_int(body)
change_values_from_body_to_bool(body)
