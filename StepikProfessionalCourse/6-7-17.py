from collections import Counter
print(*[f'{i[0]}: {i[1]}' for i in sorted(Counter(input().split(',')).items(), key= lambda x: x[0])], sep='\n')