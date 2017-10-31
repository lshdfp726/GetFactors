#! /usr/bin/env python
#  -*- coding:UTF8 -*-

'isprime'

def prime(number):
	count = number / 2
	'prime judge'
	while count > 1:
		if number % count == 0:
			return False
		count -= 1
	else:#cycle over and not interrupt by break!
		return True


if __name__ == '__main__':
	promt = 'please input a number: '
	number = int(raw_input(promt))
	print prime(number)