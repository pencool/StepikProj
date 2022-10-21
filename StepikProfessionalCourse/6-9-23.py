from collections import ChainMap, Counter

bread = {'булочка с кунжутом': 15, 'обычная булочка': 10, 'ржаная булочка': 15}
meat = {'куриный бифштекс': 50, 'говяжий бифштекс': 70, 'рыбный бифштекс': 40}
sauce = {'сливочно-чесночный': 15, 'кетчуп': 10, 'горчица': 10, 'барбекю': 15, 'чили': 15}
vegetables = {'лук': 10, 'салат': 15, 'помидор': 15, 'огурцы': 10}
toppings = {'сыр': 25, 'яйцо': 15, 'бекон': 30}

menu = ChainMap(bread, meat, sauce, vegetables, toppings)
order = Counter(input().split(','))
space = len(max(order, key=len))
total = 0
for k, v in sorted(order.items()):
    total += menu[k] * v
    print(f'{k.ljust(space)} x {v}')
print('-'*(max([(space + 3 + len(str(max(order.values())))), (7 + len(str(
    total)))])))
print(f'ИТОГ: {total}р')