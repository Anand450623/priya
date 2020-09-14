import json


def reader(path):

    with open(path, "r") as f:
        data = json.load(f)

    for item in data:
        print(item['id'], item['name'])
