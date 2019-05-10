"""
Implementing 6 exercises from chapter 11.
A menu for selecting the exercise to run is shown on start and after
exercise has ended. If no valid exercise number was selected more
than the number of specified tries, program will exit (with code 1).
"""

from math import gcd
from random import randint
from re import search


def get_int_input(prompt='Please enter integer:\n', tries=3):
    """
    Get user input for an integer, checking it has only digits and
    an optional +/- as prefix. Converting the input string to integer.
    Note - if no valid input (integer) is received from user in more
    than the allowed "tries", program will exit (with code 1).
    :param prompt: message string to display.
    :param tries: number of tries, for invalid input, before aborting.
    :return: the given integer.
    """
    while tries > 0:
        tries -= 1
        user_input = input(prompt)
        if not search('^-?\d+$', user_input):
            print(f'Not a valid number. Please use digits only and the optional +/- as prefix. You have {tries} more tries.')
            continue
        else:
            return int(user_input)

    print('You failed to enter a valid integer. No more tries. Aborting.')
    exit(1)


def biggest_of_10_numbers():
    """
    Asking user to enter 10 numbers, then outputting the biggest
    :return: None
    """
    print("Enter 10 numbers and we'll tell you which is the biggest.")
    numbers = []
    for i in range(1, 11):
        new_input = get_int_input(f'{i}. Please enter number: ')
        numbers.append(new_input)
    print('Maximal entered number is: ', max(numbers))


def age_in_months():
    """
    Prompting for age in years. Calculate and print age in months.
    :return: None
    """
    age_in_years = get_int_input('Please enter your age in years: ')
    print(f'Your age in months is [at least] {age_in_years * 12} months.')


def revers_lines():
    """
    Asking user to enter multiple lines of text, ending with blank line.
    Output given lines in revers order.
    :return: None
    """
    print('''
Please enter lines of text.
Finish by entering a blank line, then we'll print them in reverse order''')
    lines = []
    while True:
        line = input()
        if '' == line:
            break
        lines.append(line)

    # option #1 lines.reverse()
    # option #2 revers range
    # for i in range(len(lines) - 1, -1, -1):
    #    print(lines[i])
    # option #3 reverse list inline
    for i in lines[::-1]:
        print(i)


def find_random_divides_by(to_divide_by=[7, 13, 15], min_range=1, max_range=1000000, max_iterations=1000000):
    """
    Given a few numbers, fined and return a random number that can be divided by them.
    :param to_divide_by: a list of numbers the number should be divided by.
    :param min_range: minimal range for the random number.
    :param max_range: maximal range for the random number.
    :param max_iterations: maximal number of iterations before calling it quits (and returning 0).
    :return: None
    """
    tested = []
    iterations = 0
    while max_iterations > iterations:
        iterations += 1
        cur_num = randint(min_range, max_range)
        if cur_num in tested:
            continue
        tested.append(cur_num)
        for i in to_divide_by:
            if 0 != cur_num % i:
                break
        else:
            print('{} can be divided by: {} (found after {} '
                  'iterations).'.format(cur_num, ", ".join(str(i) for i in to_divide_by), iterations))
            return None

    print('Found no number that can be divided by: {} '
          '(after {} iterations).'.format(", ".join(str(i) for i in to_divide_by), iterations))


def find_lcm_of_random_numbers(min_range=1, max_range=10):
    """
    Randomly generate 2 numbers and find their LCM
    :param min_range: minimal range for the random numbers.
    :param max_range: maximal range for the random numbers.
    :return: None
    """
    num1 = randint(min_range, max_range)
    num2 = randint(min_range, max_range)
    gcd_of_nums = gcd(num1, num2)
    lcm_of_nums = num1 * num2 / gcd_of_nums
    print(f'The LCM of {num1} and {num2} is: {lcm_of_nums:g}.')


def number_guessing_game(min_range=1, max_range=100, max_tries=7, glitch_percentage=10):
    """
    A number guessing game where the user is asked to guess
    a randomly generated number within a fixed number of tries.
    :param min_range: minimal range for the random number.
    :param max_range: maximal range for the random number.
    :param max_tries: maximal number of tries before game is lost.
    :param glitch_percentage: the chance percentage for a "glitch" in the feedback.
    :return: None
    """
    num_to_guess = randint(min_range, max_range)
    print(f'A random number between {min_range} and {max_range} was generated.')
    while max_tries > 0:
        glitch = True if randint(1, 100) <= glitch_percentage else False
        guess = get_int_input('You have {} {}, guess: '.format(max_tries, 'try' if 1 == max_tries else 'tries'))
        max_tries -= 1
        if guess == num_to_guess:
            print(f'Great success! You found the number with {max_tries}', 'try' if 1 == max_tries else 'tries', 'remaining.')
            return None
        elif guess > num_to_guess:
            print(f'{guess} is too', 'small IMHO.' if glitch else 'big.')
        else:
            print(f'{guess} is too', 'big IMHO.' if glitch else 'small.')

    print(f'No more tries. You failed to guess the number. It was: {num_to_guess}.')


tries = 3
while True:
    print('''
Please select the exercise to run:
1. The biggest of 10 numbers.
2. Age in months.
3. Reverse lines.
4. Find a random number (range: 1-1,000,000) that divides by 7, 13 and 15.
5. Find least common multiple of 2 random numbers (range: 1-10).
6. Number guessing game.
0. Exit.''')
    selected_task = get_int_input('')
    if 0 == selected_task:
        print('Goodbye. Exiting.')
        exit()
    elif 1 == selected_task:
        biggest_of_10_numbers()
    elif 2 == selected_task:
        age_in_months()
    elif 3 == selected_task:
        revers_lines()
    elif 4 == selected_task:
        find_random_divides_by()  # ([2, 3, 7], 1, 100, 8)
    elif 5 == selected_task:
        find_lcm_of_random_numbers()
    elif 6 == selected_task:
        number_guessing_game()
    else:
        tries -= 1
        print('No valid option was selected.', end=' ')
        if tries > 0:
            print(f'You have {tries} more', 'tries.' if tries > 1 else 'try.')
            continue
        else:
            print('You have no more tries.')
            exit(1)

