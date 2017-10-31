#! /usr/bin/env python
#  -*- coding:UTF* -*-

'return factors'

import isPrime

def getfactors(number):
	array = []
	count = number / 2
	
	while count > 1:
		if number % count == 0:
			array.append(count)
		count -= 1
	else:
		array.extend([1,number])
		return array

if __name__ == '__main__':
	promot = 'please input a number: '
	number = int(raw_input(promot))
	result = isPrime.prime(number)
	if result == False: #不是素数,返回所有约束，包含1 和其本身
		print getfactors(number)


		