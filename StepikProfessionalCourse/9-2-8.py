def hash_as_key(objects: list):
    out = {}
    for i in objects:
        if out.get(hash(i)):
            if isinstance(out.get(hash(i)), list):
                out.get(hash(i)).append(i)
            else:
                out[hash(i)] = [out[hash(i)]] + [i]
        else:
            out.setdefault(hash(i), i)
    return out


data = [1, 2, 3, 4, 5, 5, 5, 5]

print(hash_as_key(data))
