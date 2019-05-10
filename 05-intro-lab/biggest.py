import re

numbers = []
print('Please enter 3 numbers')
enter_numbers_label = ['first', 'second', 'third']
for i in range(3):
    user_input = False
    while not user_input:
        user_input = input(f'Please enter {enter_numbers_label[i]} number:\n')
        if not re.search('^-?\d+$', user_input):
            print('Not a valid number.')
            user_input = False

    numbers.append(int(user_input))

print('Maximum is: ', max(numbers))
