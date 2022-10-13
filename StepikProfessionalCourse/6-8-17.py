from collections import Counter

data = Counter('aksjaskfjsklfjdslkfjajfopewtoieqpwdpqworiiqjskanvmcxbmpewrqopkqwlmdzczmxvmvlnjpjqpkqzxvmbowiqeorewi')
data.min_values = lambda: [*filter(lambda x: x[1] == min(data.values()),
                                  data.most_common())]
data.max_values = lambda: [*filter(lambda x: x[1] == max(data.values()),
                                  data.most_common())]
print(data.max_values())