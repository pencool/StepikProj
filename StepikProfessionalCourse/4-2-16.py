import csv

with open('data.csv', 'r', encoding='utf-8', newline='') as f, open(
        'domain_usage.csv', 'w', encoding='utf-8', newline='') as out:
    read = csv.DictReader(f)
    write = csv.writer(out)
    result = {}
    for i in read:
        result[i['email'].split('@')[1]] \
            = result.get(i['email'].split('@')[1], 0) + 1
    write.writerow(['domain', 'count'])
    write.writerows(sorted(sorted(zip(result.keys(), result.values())),
                           key=lambda x: x[1]))