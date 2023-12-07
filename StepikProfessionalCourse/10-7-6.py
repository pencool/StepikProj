def parse_ranges(ranges: str):
    parse_diap = (i.split('-') for i in ranges.split(','))
    res = (j for i in parse_diap for j in range(int(i[0]), int(i[1])+1))
    return res

print(*parse_ranges('1-10,2-10'))