with open('bla.txt', 'r', encoding='UTF-8') as f:
    first_line: str = f.readline()
    print(f'1st line: "{first_line}"')
    for line in f:
        print(line, end='')

    # automatically call f.close()

print('\nappending lines')
with open('bla.txt', 'a', encoding='UTF-8') as f:
    f.write('Appending lines\n')
    f.writelines([
        'line number 1\n',
        'line number 2\n',
        'line number 3\n',
        'line number 4\n',
        'line number 5\n',
    ])

print('\nUpdated file:')
with open('bla.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        print(line, end='')
