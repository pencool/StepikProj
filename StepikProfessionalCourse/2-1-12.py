def spell(*args):
    result = {}
    for i in args:
        if i[0].lower() not in result or len(i) > result[i.lower()[0]]:
            result[i.lower()[0]] = len(i)
    return result

words = ['fruit', 'football', 'February', 'forest', 'Family']
print(spell(*words))