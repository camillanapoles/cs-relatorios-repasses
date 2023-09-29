import json
import os

def check_file_exists(filename):
    return os.path.isfile(f'data_analytics/listas/{filename}.json')

def create_directory():
    if not os.path.exists('data_analytics/listas'):
        os.makedirs('data_analytics/listas')

def export_list(lista, filename):
    json_string = json.dumps(lista)
    with open(f'data_analytics/listas/{filename}.json', 'w') as f:
        json.dump(lista, f)

def append_list(lista, filename):
    json_string = json.dumps(lista)
    with open(f'data_analytics/listas/{filename}.json', 'a') as f:
        json.dump(lista, f)

def import_list(filename):
    with open(f'data_analytics/listas/{filename}.json', 'r') as f:
        return json.load(f)
