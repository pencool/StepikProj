def read_csv():
    with open('data.csv') as f:
        data = [i.strip().split(',') for i in f]
        out = []
        for i in data[1:]:
            out.append(dict(zip(data[0], i)))
        return out


print(read_csv())
