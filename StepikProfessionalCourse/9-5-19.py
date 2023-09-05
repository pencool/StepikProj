from datetime import date

dates = {
    'ru': '%d.%m.%Y',
    'us': '%m-%d-%Y',
    'ca': '%Y-%m-%d',
    'br': '%d/%m/%Y',
    'fr': '%d.%m.%Y',
    'pt': '%d-%m-%Y'
}


def date_formatter(country_code):
    def format_date(dt):
        return dt.strftime(dates[country_code])

    return format_date


date_ru = date_formatter('ru')
today = date(2022, 1, 25)
print(date_ru(today))
