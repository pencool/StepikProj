from datetime import date
print(*[i.strftime('%d/%m/%Y') for i in sorted([date.fromisoformat(input()) for i in range(int(input()))])], sep='\n')