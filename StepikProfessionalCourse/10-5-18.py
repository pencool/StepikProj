def reverse(sequence):
    for i in sequence[::-1]:
        yield i


generator = reverse('beegeek')

print(type(generator))
print(*generator)
