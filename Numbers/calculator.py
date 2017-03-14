def precendence(symbol):
	precendences = {
		"(" : 0,
		")" : 0,
		"#" : 1,
		"+" : 2,
		"-" : 2,
		"*" : 3,
		"/" : 3,		
		"^" : 4
	}
	return precendences[symbol]

def isOperator(symbol):
	if(symbol in ["(", ")", "+", "-", "*", "/"]):
		return True
	else:
		return False

def convertToPostfix(infix):
	postfix = []
	stack = []
	stack.append("#")
	for symbol in infix:
		if(isOperator(symbol) == False):
			postfix.append(symbol)
		else:
			if(symbol == "("):
				stack.append("(")
			elif(symbol == ")"):
				while(stack[-1] != "("):
					postfix.append(stack.pop())
				stack.pop()
			else:
				if(precendence(symbol) >= precendence(stack[-1])):
					stack.append(symbol)
				else:
					while (precendence(symbol) < precendence(stack[-1])):
						postfix.append(stack.pop())
					stack.append(symbol)


	while(stack[-1] != "#"):
		postfix.append(stack.pop())
	return postfix

def evaluatePostfix(postfix):	
	stack = []
	for symbol in postfix:
		if(isOperator(symbol)):
			operand1 = int(stack.pop(1))
			operand2 = int(stack.pop())
			result = math(symbol, operand1, operand2)
			stack.append(result)
		else:
			stack.append(symbol)
	return stack[0]


def math(symbol,a,b):
	operations = {
		"+" : add,
		"-" : subtract,
		"*" : multiply,
		"/" : divide
	}
	return operations[symbol](a,b)

def add(a,b):
	return a+b

def subtract(a,b):
	return a-b

def multiply(a,b):
	return a*b

def divide(a,b):
	return a/b

if __name__ == '__main__':
	infix = input('Enter arithematic expression to be evaluated : ')
	postfix = convertToPostfix(list(infix))	
	answer = evaluatePostfix(postfix)
	print("Answer : " + str(answer))