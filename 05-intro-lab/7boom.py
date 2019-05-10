print('Enter 7 numbers, if they are divided by or contain 7, they will be replaced by "Boom!"\n')
user_input = False
for i in range(1, 8):
    while not user_input:
        user_input = input(f'{i}. Please enter a number\n')
        if not user_input.isdigit():
            print('Not a number')
            user_input = False
            continue

    if int(user_input) % 7 == 0 or '7' in user_input:
        print('Boom!\n')
    else:
        print(f'{user_input}\n')

    user_input = False
