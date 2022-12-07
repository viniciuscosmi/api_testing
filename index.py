import json
import requests

API_URL = 'http://localhost:3000/usuarios'
VALUES = [None, '', 123, True]

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

def change_values_from_body(body, value):
    for k, v in body.items():
        if isinstance(v, dict):
            change_values_from_body(v, value)
        elif isinstance(v, list):
            change_values_from_body(v[0], value)
        else:
            initial_value = body[k]
            body[k] = value
            send_request()
            body[k] = initial_value

for i in VALUES:
    change_values_from_body(body, i)
