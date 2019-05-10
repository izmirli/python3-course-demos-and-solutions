import fileinput
import argparse

parser = argparse.ArgumentParser(description='Count unique words from a file.')
parser.add_argument('--file', '-f', default='story.txt')
parser.add_argument('--case-insensitive', '-c', action='store_true', dest='casefold')
args = parser.parse_args()

unique_words = set()
overall_words = 0
try:
    for line in fileinput.input(args.file):
        if args.casefold:
            line = line.casefold()
        words = line.split()
        unique_words.update(words)
        print(f'[num of words: {len(words)}]: ', words)
        overall_words += len(words)
except FileNotFoundError as e:
    print(f'Failed to read from file -', e, '\nAborting.')
    exit(1)

print(f'Number of unique_words: {len(unique_words)}')
print(f'Number of overall_words: {overall_words}')
