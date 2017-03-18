row = 0;
answer = []

def evaluatePascal(size, prevList):
	if(size == 0):
		return answer
	loopAnswer = []
	loopAnswer.append(1)
	for i in range(len(prevList) - 1):
		loopAnswer.append(prevList[i] + prevList[i+1])

	loopAnswer.append(1)
	answer.append(loopAnswer)
	return evaluatePascal(size - 1, loopAnswer)

def printPascalTriangle(size,data):
	#print(data)
	if(size == 0):
		return data
	print(" "*size + " ".join([str(i) for i in data[0]]) + " "*size)
	data.pop(0)
	return printPascalTriangle(size-1,data)


if __name__ == "__main__":
	answer = []
	answer.append([1])
	answer.append([1,1])
	size = int(input("Enter Pascal's triangle length : "))
	row = size
	pascalArr = evaluatePascal(size-2, answer[-1])
	printPascalTriangle(size, pascalArr)