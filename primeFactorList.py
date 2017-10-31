#! /usr/bin/env python 
#  -*- coding:UTF8 -*-

'prime factor'

import isPrime 
import getFactors 

primefactorArray = [] #一个数的质因数列表

def primeFactorList(number):
	'get prime factor list'
	if isPrime.prime(number):#如果是质数，返回1和其本身
		return [1,number]
	else:
		array = getFactors.getfactors(number)
		array.remove(1)
		array.remove(number) 
		global primefactorArray 
		temArray = [x for x in array if isPrime.prime(x)]#一个数的质因数数集合
		primefactorArray.extend(temArray)#添加到质数因数列表
		temp = 1 #质数的乘积
		for x in temArray:
			temp *=x

		if temp == number:#如果temp 已经等于number，那么已经是质因数成积
			return primefactorArray
		else:#利用number 和 temp 商在进行分解
			return getProductList(number,temp)


def getProductList(number,temp):
	'get product list'
	global primefactorArray
	x = number / temp
	if isPrime.prime(x):
		primefactorArray.append(x) #如果x 是质数 ，那么 number = temp * x （temp 已经是质数的成积了）
	else:
		primeFactorList(x)#迭代求质数

	return primefactorArray

if __name__ == '__main__':
	promot = 'plsease input a number: '
	number = int(raw_input(promot))
	print  primeFactorList(number)