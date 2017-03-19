#6,1,7,8,9,3,5,4,2

def insertion_sort(numbers, sortingIndex, length):
	if(sortingIndex == length):
		return numbers

	currentElement = numbers[sortingIndex]
	for i in range(1, sortingIndex + 1):
		if(numbers[sortingIndex - i] > currentElement):
			numbers[sortingIndex - i], currentElement = currentElement, numbers[sortingIndex - i]

	return insertion_sort(numbers, sortingIndex + 1, length)


def selection_sort(numbers, sortingIndex, length):
	if(sortingIndex == length - 1):
		return numbers

	minVal = min(numbers[sortingIndex:])
	swapIndex = numbers.index(minVal)
	numbers[sortingIndex], numbers[swapIndex] = numbers[swapIndex], numbers[sortingIndex]
	
	return selection_sort(numbers, sortingIndex + 1, length)


def bubble_sort(numbers, length):
	right = -1
	left = -2
	swap = False
	for i in range(length - 1):
		if(numbers[left - i] > numbers[right - i]):
			numbers[left - i], numbers[right - i] = numbers[right - i], numbers[left - i]
			swap = True

	if(swap == False):
		return numbers
	
	return bubble_sort(numbers, length)


if __name__ == "__main__":
	userInput = list(input("Enter comma separated numbers to be sorted : "))
	length = len(userInput)

	print("\nBubble Sorting")
	bubbleSorted = bubble_sort(userInput, length)
	print(bubbleSorted)

	print("\nSelection Sorting")
	selectionSorted = selection_sort(userInput, 0, length)
	print(selectionSorted)

	print("\nInsertion Sorting")
	insertionSorted = selection_sort(userInput, 1, length) #0th index is sorted
	print(insertionSorted)