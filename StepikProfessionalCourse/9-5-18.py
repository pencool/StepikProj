def sourcetemplate(url):
    url += '?'

    def foo(**kwargs):
        nonlocal url
        for k, v in sorted(kwargs.items()):
            url += f'{k}={v}&'
        return url.rstrip('&?')

    return foo


url = 'https://all_for_comfort_life.com'
load = sourcetemplate(url)
print(load(smartphone='iPhone', notebook='huawei', sale=True))
