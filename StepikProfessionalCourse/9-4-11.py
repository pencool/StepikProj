def numbers_sum(elems):

	"""Принимает список и возвращает сумму его чисел (int, float),
	игнорируя нечисловые объекты. 0 - если в списке чисел нет."""
	return sum(filter(lambda x: type(x) in (int, float), elems))


print(numbers_sum(['beegeek', 'stepik', '100']))