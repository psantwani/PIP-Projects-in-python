# Take the first element of the array, ie 2 and eliminate all multiples of 2 of the table.
# Then take the next number not eliminated, here 3 and remove multiples of 3.
# Then take the next number not eliminated, here 5 (because 4 was eliminated in the first step) and eliminate multiples of 5.
# and so on...
# At the end all non-primes are eliminated

answer = []

def printPrimeNumbers(numbers):
	if(len(numbers) == 0):
		print(answer)
		return 0
	first = numbers[0]
	answer.append(first)
	matches = []
	for i in numbers:
		if(i%first == 0):
			matches.append(i)

	printPrimeNumbers([x for x in numbers if x not in matches])

	
if __name__ == "__main__":
	while EOFError:
		answer = []
		max_int = int(input("Get all prime numbers from 0 to : "))
		numbers = range(2,max_int + 1)
		printPrimeNumbers(numbers)