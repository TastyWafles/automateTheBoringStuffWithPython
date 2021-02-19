def collatz(number):
    if number == 1:
        print('Collatz complete')
    elif number % 2 == 0:
        print(int(number / 2))
        collatz(number / 2)
    else:
        print(int(number * 3 + 1))
        collatz(number * 3 + 1)

print('Enter Number:')
number = int(input())
collatz(number)
