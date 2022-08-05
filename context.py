a = int(input())
b = input().split()
z = dict(zip(set(b), [0] * len(set(b))))
ans = [0, 0]
for i in set(b):
    z[i] = b.count(i)
for k,v in z.items():
    if ans[1] < v:
        ans = [int(k), v]
    if ans[1] == v:
        ans[0] = max([int(k), ans[0]])
print(ans[0])
#print(sorted([*filter(lambda x: x[1] == max(z.values()), z.items())], key=lambda q: q[0], reverse=True)[0][0])
