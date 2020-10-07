""" Sum of Integers Up To n
    Write a function, add_it_up().

    prompt user to take a single integer as input.
    And then returns the sum of the integers from zero to the input parameter.

    The function should return 0 if a non-integer is passed in.
"""


def add_it_up():
    try:
        nth = int(input('Enter an integer: '))
        total = sum(range(nth + 1))
    except ValueError:
        print('Please enter an integer.')
        total = 0
    return total


integers_sum = add_it_up()
print(f'Total: {integers_sum}')
