import csv

with open('sales.csv', 'r', encoding='utf-8', newline='') as f:
    reader = csv.DictReader(f, delimiter=';')
    have_sale = filter(lambda x: int(x['old_price']) > int(x['new_price']), reader)
    for i in have_sale:
        print(i['name'])
