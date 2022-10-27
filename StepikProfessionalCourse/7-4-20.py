import json

try:
    with open(input(), encoding='utf-8') as f:
        print(json.load(f))
except FileNotFoundError:
    print('Файл не найден')
except json.decoder.JSONDecodeError:
    print('Ошибка при десериализации')