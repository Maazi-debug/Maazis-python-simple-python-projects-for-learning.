ret_number = 0
def collatz(number):
    if number % 2 == 0:
       ret_number = number // 2

    else:
        ret_number = 3 * number + 1

    print(ret_number)
    return ret_number

number = int(input('Enter number: '))

while number != 1:
    number = collatz(number)

