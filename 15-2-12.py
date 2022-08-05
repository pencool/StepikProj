def greet(name, *args):
    return 'Hello, ' + ''.join(name) +' and '+ ' and '.join(args) + '!' if len(args) > 0 else 'Hello, ' + ''.join(name) + '!'


print(greet('Soltan'))