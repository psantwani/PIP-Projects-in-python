import sys

def binaryToDecimalConvertor(number):
	num = list(number)
	num.reverse()
	answer = 0
	for i in range(len(num)):
		answer += int(num[i])*(2**i)
	return str(answer)

def decimalToBinaryConvertor(number):
	answer = []
	num = int(number)
	a = num
	while a > 0:
		b = a%2
		answer.append(str(b))
		a = a//2	
	return ''.join(list(reversed(answer)))

def quit():
	sys.exit("Quitting...")

if __name__ == '__main__':
	print('Select operation - \n 1:Convert binary to decimal \n 2:Convert decimal to binary \n 3:Quit ')
	operation = 0
	while operation != 3 or EOFError:		
		operation = input('Your choice: ')		
		if operation == '3':			
			quit()
		
		question = input("Enter number : ")
		convertor = {
			'1' : binaryToDecimalConvertor,
			'2' : decimalToBinaryConvertor,			
		}

		ans = convertor[operation](question)
		print("Answer: " + ans)
		print("---------------")