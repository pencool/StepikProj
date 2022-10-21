from collections import Counter

books = Counter(map(int, input().split()))
total = 0
for i in range(int(input())):
    sell, price = input().split()
    if books[int(sell)] > 0:
        books.subtract(Counter([int(sell)]))
        total += int(price)
print(total)