def polynom(x):
	result = x * x + 1
	polynom.values.add(result)
	return result


polynom.__dict__['values'] = set()

print(polynom(5))
print(polynom.values)
