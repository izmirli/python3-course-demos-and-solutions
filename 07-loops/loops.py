for i in range(1,11):
    for j in range(1, 11):
        print(f'{i * j}\t', end='')

    print()

while True:
    name = input('Who are you? ')
    if name.startswith('O'):
        break
    print(f'{name} doesn\'t start with O')

print(f'name: {name}. Ta Da!')
