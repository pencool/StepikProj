from collections import defaultdict, OrderedDict


def best_sender(messages: list, senders: list) -> str:
    senders_messages = defaultdict(int)
    for k, v in zip(senders, messages):
        senders_messages[k] += len(v.split(' '))
    return max(senders_messages.items(), key=lambda x: (x[1], x[0]))[0]



messages = ['How is Stepik for everyone', 'Stepik is useful for practice']
senders = ['Bob', 'Charlie']

print(best_sender(messages, senders))


print(OrderedDict(),
OrderedDict(name='Timur', surname='Guev', hobby='math'),
OrderedDict({'name': 'Timur', 'surname': 'Guev', 'hobby': 'math'}),
OrderedDict((['name', 'Timur'], ['surname', 'Guev'], ['hobby', 'math'])),
OrderedDict.fromkeys(('name', 'surname', 'hobby'), 'Empty'))