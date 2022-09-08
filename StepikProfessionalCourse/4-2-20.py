import csv


def condense_csv(filename, id_name):
    with open(filename) as f, open('condensed.csv', 'w',
                                   encoding='utf-8') as n:
        new_d = {}
        out_d = {}
        for i in csv.reader(f):
            new_d.setdefault(i[1], []).append([i[0], *i[2:]])
        writer = csv.writer(n)
        writer.writerow([id_name, *new_d.keys()])
        for i in new_d.values():
            for j in i:
                out_d.setdefault(j[0], []).append(*j[1:])
        for k, v in out_d.items():
            writer.writerow([k, *v])


text = '''01,Artist,Otis Taylor
01,Title,Ran So Hard the Sun Went Down
01,Time,3:52
02,Artist,Waylon Jennings
02,Title,Honky Tonk Heroes (Like Me)
02,Time,3:29'''

with open('data.csv', 'w', encoding='utf-8') as file:
    file.write(text)

condense_csv('data.csv', id_name='ID')

with open('condensed.csv', encoding='utf-8') as file:
    print(file.read().strip())
