def top_grade(grades: dict[str, str | list[int]]) -> dict[str, str | int]:
    ans = {}
    ans['name'] = grades['name']
    ans['top_grade'] = max(grades['grades'])
    return ans



print(*top_grade.__annotations__.values())
