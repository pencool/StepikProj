import csv

with open('student_counts.csv', encoding='utf-8') as f, open(
        'sorted_student_counts.csv', 'w', encoding='utf-8', newline='') as n:
    reader = csv.DictReader(f)
    cols = sorted(sorted(reader.fieldnames[1:]), key=lambda y: -int(
            y.split('-')[0]), reverse=True)
    out = list(reader)
    headers = ['year', *cols]
    writer = csv.DictWriter(n, fieldnames=headers)
    writer.writeheader()
    writer.writerows(out)
