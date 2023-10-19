def get_min_max(data):
    if data:
        indexing = list(enumerate(data))
        return (min(indexing, key=lambda x: x[1])[0],
                max(indexing, key=lambda x: x[1])[0])

data = [2, 3, 8, 1, 7]

print(get_min_max(data))