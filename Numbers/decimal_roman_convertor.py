from math import floor

def divMod(number, i):
	return floor(number/i), number%i

def decimalToRoman(number):
	symbols = {
		1 : "I",
		5 : "V",
		10 : "X",
		50 : "L",
		100 : "C",
		500 : "D",
		1000 : "M"
	}

	denominations = list(symbols)
	denominations.sort()
	answer = []
	for i in reversed(denominations):
		while(number >= i and number%i >= 0):
			times, number = divMod(number, i)
			answer.append(symbols[i]*times)
		if(number == 0):
			break

	return "".join(answer)

if __name__ == "__main__":
	while EOFError:
		decimal = int(input("Enter integer : "))
		roman = decimalToRoman(decimal)
		print("Answer : " + roman)
	