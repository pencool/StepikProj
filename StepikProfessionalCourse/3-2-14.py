from datetime import date

def print_good_dates(dates):
        return print(*[i.strftime('%B %d, %Y') for i in sorted(dates) if i.year == 1992 and sum([i.day, i.month]) == 29], sep='\n')

dates = [date(1992, 10, 19), date(1991, 12, 6), date(1992, 9, 20)]
print_good_dates(dates)