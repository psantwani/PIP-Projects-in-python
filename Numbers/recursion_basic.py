def printArrInput():
	elements = input('Enter array elements : ')
	printArr(elements.split(","))	

def printArr(arr):	
	if(len(arr) < 1):	
		return
	print('Printing {0}'.format(arr[0]))
	arr = arr[1:]
	printArr(arr)

def palindromeInput():
	word = input('Input string : ')
	reversedString = reverse(word)
	if(reversedString == word):
		print('Entered string is a palindrome')
	else:
		print('Entered string is not a palindrome')

def powerInput():
	print('Enter a and b to perform a to the power b')
	a = int(input('Enter a : '))
	b = int(input('Enter b : '))
	answer = power(a,b)
	print(answer)

def power(a,b):
	if b < 2:
		return a
	return power(a, b - 1)*a

def reverse(word):	
	if(len(word) < 2):		
		return word	
	return reverse(word[1:len(word)]) + word[0]

if __name__ == '__main__':
	print(
		"1. Go through an array and print out all of the elements\n" +
		"2. Determine whether or not a string is a palindrome\n" +
		"3. Calculate a raised to the power of b\n"		
		)
	
	methods = {
		"1" : printArrInput,
		"2" : palindromeInput,
		"3" : powerInput,
		"4" : quit
	}

	choice = 0
	
	while EOFError or choice == "4":
		choice = input("your choice : ");
		methods[choice]()