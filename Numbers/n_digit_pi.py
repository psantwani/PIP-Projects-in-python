import math

def calculatePi(digits):
	pi = math.atan(1)*4
	print("Answer : " + str(pi)[:digits])



if __name__ == "__main__":
	while EOFError:
		digits = input('Please enter how many digits of PI you would like to see (Max 20): ')
		calculatePi(int(digits) + 1)