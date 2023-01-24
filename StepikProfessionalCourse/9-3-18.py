from string import ascii_lowercase as al, ascii_uppercase as au, digits as dig


def verification(login, password, success, failure):
	if len(set(password).intersection(set(al).union(au))) < 1:
		return failure(login, text='в пароле нет ни одной буквы')
	elif len(set(password).intersection(au)) < 1:
		return failure(login, text='в пароле нет ни одной заглавной буквы')
	elif len(set(password).intersection(al)) < 1:
		return failure(login, text='в пароле нет ни одной строчной буквы')
	elif len(set(password).intersection(dig)) < 1:
		return failure(login, text='в пароле нет ни одной цифры')
	return success(login)


def success(login):
    print(f'Здравствуйте, {login}!')

def failure(login, text):
    print(f'{login}, попробуйте снова. Текст ошибки: {text}')

verification('Ruslan_Chaniev', 'stepikstepik2', success, failure)