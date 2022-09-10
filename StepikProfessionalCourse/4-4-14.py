import json
import csv
from datetime import datetime

with open('exam_results.csv', encoding='utf-8') as f, open(
        'best_scores.json', 'w', encoding='utf-8') as out:
    names = ["name", "surname", "best_score", "date_and_time", "email"]
    reader = csv.DictReader(f.readlines()[1:], fieldnames=names)
    scores = {}
    for i in reader:
        scores.setdefault(i['email'], []).append(i)
    best_score = []
    for k, v in scores.items():
        for i in v:
            i['best_score'] = int(i['best_score'])
        best_score.append(sorted(sorted(v, key=lambda x:
        datetime.strptime(x['date_and_time'], '%Y-%m-%d %H:%M:%S'), reverse=True),
                                 key=lambda x: x['best_score'], reverse=True)[
                              0])
    json.dump(sorted(best_score, key=lambda x: x['email']), out, indent=3)
