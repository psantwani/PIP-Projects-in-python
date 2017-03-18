#python3 luhn_algorithm_CC_validator.py
#Try it on your Debit/Credit cards
def digits_of(number):
    return [int(i) for i in str(number)]

def luhn_checksum(card_number):
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    total = sum(odd_digits)
    for digit in even_digits:
        total += sum(digits_of(2 * digit))
    return total % 10

def is_luhn_valid(card_number):
    print("CC number is valid") if luhn_checksum(card_number) == 0 else print("CC number is invalid")

def calculate_luhn(partial_card_number): 
	print(partial_card_number)
	check_digit = luhn_checksum(int(partial_card_number) * 10)
	answer = check_digit if check_digit == 0 else 10 - check_digit
	print("check_digit : " + str(answer))

if __name__ == '__main__':
	number = input('Enter credit card number : ')
	is_luhn_valid(number)
	calculate_luhn(number[:-1])


