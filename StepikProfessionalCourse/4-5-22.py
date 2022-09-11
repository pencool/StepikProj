from zipfile import ZipFile
import json

f_payers = []
with ZipFile('data.zip') as zf:
    for i in zf.infolist():
        if not i.is_dir() and i.filename.split('/')[-1].split('.')[-1] == 'json':
            try:
                with zf.open(str(i.filename)) as f:
                    club = json.loads(f.read().decode('utf-8'))
                    if club['team'] == 'Arsenal':
                        f_payers.append([club['first_name'], club['last_name']])
            except UnicodeDecodeError:
                continue
            except json.decoder.JSONDecodeError:
                continue
for i in sorted(sorted(f_payers, key=lambda x: x[1]), key=lambda x: x[0]):
    print(*i)