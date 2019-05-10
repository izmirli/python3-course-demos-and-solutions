import sys

number_of_expected_grades = 20
grades_list = []
try:
    for i in range(1, number_of_expected_grades + 1):
        grades_list.append(int(sys.argv[i]))
except ValueError:
    print(f'Expected grades to be numerical, but grade#{len(grades_list) + 1} is: "{sys.argv[len(grades_list) + 1]}".')
    exit(1)
except IndexError:
    print(f'Expected {number_of_expected_grades} grades, but got:', len(grades_list))
    exit(2)

grades_avg = sum(grades_list) / number_of_expected_grades
above_avg = [str(g) for g in grades_list if g > grades_avg]
print('above avg grades:', ' '.join(above_avg))
