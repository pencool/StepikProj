import json


def is_correct_json(string):
    try:
        sj = json.loads(string)
        return True
    except json.decoder.JSONDecodeError:
        return False


data = '{"name": "Barsik", "age": 7, "meal": "Wiskas"}'

print(is_correct_json(data))