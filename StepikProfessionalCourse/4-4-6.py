import json
import sys

for k, v in json.loads(sys.stdin.read()).items():
    if type(v) is list:
        print(f"{k}: {', '.join(map(str, v))}")
    else:
        print(f'{k}: {v}')
