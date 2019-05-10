name = input('Who are  you?\n')
print(f"Hello! {name}. Nice to meet you.")

age = input(f'{name}, please enter your age:\n')
try:
    age_in_months = int(age) * 12
except ValueError:
    print(f'"{age}" is not a numeric age (as expected). Aborting.')
    exit(1)
print(f'{name}, your age in months is at least: {age_in_months}\n')

months_old = input(f'{name}, please enter your age in months:\n')
age_by_months = int(months_old) / 12
print('{:s}, your age according to given months is: {:.0f}.\n'.format(name, age_by_months))

print('true name') if name == 'Oren' else print('This is the end')
