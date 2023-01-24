old_print = print


def print(*args, sep=' ', end='\n'):
	return old_print(*[str.upper(i) if type(i) is str else i for i in args],
					 sep=sep.upper(), end=end.upper())


print('beegeek', [1, 2, 3], 4)
