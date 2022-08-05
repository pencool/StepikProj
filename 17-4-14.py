from datetime import timedelta

with open('logfile.txt') as log, open('output.txt', 'w') as out:
    lst = [i.split(',') for i in log.read().split('\n')]
    for i in lst:
        t1 = timedelta(hours=int(i[1].split(':')[0]), minutes=int(i[1].split(':')[1]))
        t2 = timedelta(hours=int(i[2].split(':')[0]), minutes=int(i[2].split(':')[1]))
        if t2 - t1 >= timedelta(hours=1):
            print(i[0], file=out)