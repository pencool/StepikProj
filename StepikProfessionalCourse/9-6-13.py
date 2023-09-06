infl = int | float


def get_digits(number: infl) -> list[int]:
    ans = []
    for i in str(number):
        if i.isdigit():
            ans.append(int(i))
    return ans


annotations = get_digits.__annotations__

print(annotations['return'])
