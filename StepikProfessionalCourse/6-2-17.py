from string import ascii_lowercase as al
tbl = str.maketrans({k: v for k, v in zip(al, input())})
print(input().lower().translate(tbl))
