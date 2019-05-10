import re


def get_int_input(prompt='Please enter integer:\n'):
    user_input = False
    while not user_input:
        user_input = input(prompt)
        if not re.search('^-?\d+$', user_input):
            print('Not a valid number.')
            user_input = False

    return int(user_input)


first_member = get_int_input('Please enter the first member of the arithmetic progression:\n')
difference = get_int_input('Please enter the difference:\n')
num_of_members = get_int_input('Please enter the number of members:\n')

members = []
for i in range(num_of_members):
    this_member = first_member + (i * difference)
    members.append(this_member)

print(members)
print('Sum of AP is: ', sum(members))
print('Arithmetic sum of AP is: ', (num_of_members * (2 * first_member + (num_of_members - 1) * difference)) / 2)
