def generator_square_polynom(a, b, c):
    def foo(x):
        return a*x**2 + b*x + c
    return foo

f = generator_square_polynom(1, 2, 1)
print(f(5))