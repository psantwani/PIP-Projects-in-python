import math
def getNextPrime(number):
	max_int = math.floor(math.sqrt(number)) + 1
	divisor = 0
	for i in range(2, max_int):
		if(number%i == 0):
			divisor = i
			break
	if(divisor == 0):
		print(number)
		return number
	else:
		return getNextPrime(number + 1)
	


if __name__ == "__main__":
	while EOFError:
		number = int(input("Enter a number : "))
		answer = getNextPrime(number + 1)
		print("Next prime number is : " + str(answer))