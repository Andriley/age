driving = input ('have you drive before? ')
if driving != 'yes' and driving != 'no':
	print('input yes/no')
	raise SystemExit

age = input('what is your age? ')
age = int(age)
if driving == 'yes':
	if age >= 18:
		print('you pass the test')
	else:
		print('not good')
elif driving == 'no':
	if age >= 18:
		print('you can apply for test')
	else:
		print('good')
