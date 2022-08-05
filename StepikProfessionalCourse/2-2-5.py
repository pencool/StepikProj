result = {}
for k, v in {str(i): str(sum([*map(int, str(i))])) for i in range(1, int(input())+1)}.items():
    result.setdefault(v, []).append(k)
print(len(max(result.values(), key=len)))