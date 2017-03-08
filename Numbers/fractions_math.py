from functools import reduce
import sys

def getNumeratorAndDenominator(numbers):
	num = []
	den = []
	for x in numbers:
		parts = x.split("/")
		num.append(int(parts[0]))
		den.append(int(parts[1]))
	return num,den

def gcd(x,y):
	if(x > y):
		a = x
		b = y
	else:
		b = x
		a = y
	while b != 0:
		a,b = b, a%b
	return a	

def add(numbers):	
	num, den = getNumeratorAndDenominator(numbers)	
	prod = reduce(lambda x, y: x*y, den)
	total = 0
	for x in range(len(num)):
		total += int(num[x]*prod/den[x])
	hcf = gcd(total, prod)	
	return '{0}/{1}'.format(str(int(total/hcf)),str(int(prod/hcf)))

def subtract(numbers):
	num, den = getNumeratorAndDenominator(numbers)	
	prod = reduce(lambda x, y: x*y, den) 
	total = 0
	for x in range(len(num)):
		total -= int(num[x]*prod/den[x])
	hcf = gcd(total, prod)	
	return '{0}/{1}'.format(str(int(total/hcf)),str(int(prod/hcf)))

def multiply(numbers):
	num, den = getNumeratorAndDenominator(numbers)	
	numProd = reduce(lambda x, y: x*y, num)
	denProd = reduce(lambda x, y: x*y, den)
	hcf = gcd(numProd, denProd)	
	return '{0}/{1}'.format(int(numProd/hcf),int(denProd/hcf))

def divide(numbers):
	num, den = getNumeratorAndDenominator(numbers)	
	numProd = reduce(lambda x, y: x*1/y, num)
	denProd = reduce(lambda x, y: x*1/y, den)
	hcf = gcd(numProd, denProd)	
	return '{0}/{1}'.format(int(numProd/hcf),int(denProd/hcf))

def quit():
	sys.exit("Quitting..")

if __name__ == '__main__':
	print('Select operation - \n 1:add \n 2:subtract \n 3:multiply \n 4:divide \n 5:Quit')
	operation = 0
	while operation != 5 or EOFError:		
		operation = input('Your choice: ')		
		if operation == '5':			
			quit()

		fractions = input("Enter fractions(comma separated): ").split(",")	
		math = {
			'1' : add,
			'2' : subtract,
			'3' : multiply,
			'4' : divide
		}

		ans = math[operation](fractions)
		print("Answer: " + ans)
		print("---------------")