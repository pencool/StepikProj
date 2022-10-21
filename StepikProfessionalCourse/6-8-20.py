from collections import Counter


def print_bar_chart(data, mark):
    for k, v in sorted(Counter(data).items(), key=lambda x: x[1], reverse=True):
        print(f'{k.ljust(len(max(Counter(data), key=len)))} |{mark*v}')

languages = ['java', 'java', 'python', 'C++', 'assembler', 'java', 'C++', 'C', 'pascal', 'C++', 'pascal', 'java']
print_bar_chart(languages, '#')
