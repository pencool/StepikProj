import re


def remove_marks(text, marks):
	remove_marks.count += 1
	if marks == '':
		return text
	return re.sub(fr'[{marks}]', r'', text)


remove_marks.count = 0

text = 'Application for drivers!'
marks = ''
print(remove_marks(text, marks))
print(remove_marks.count)
