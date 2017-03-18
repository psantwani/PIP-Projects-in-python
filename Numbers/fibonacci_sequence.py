seq = []

def generateFibonacciSeq(size):
	if size == 0:
		return seq
	seq.append(sum(seq[-2:]))
	size -= 1
	return generateFibonacciSeq(size)


if __name__ == "__main__":
	while EOFError:
		seq = []
		seq.append(0)
		seq.append(1)
		size = int(input("Enter fibonacci size : "))
		answer = generateFibonacciSeq(size - 2)
		print(answer)