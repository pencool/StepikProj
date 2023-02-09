def power(degree: int):
    def foo(x: int):
        return x ** degree

    return foo


square = power(2)
print(square(5))
