"""Print anagrams from file

This script gets a text file (UTF-8) with 1 word in each line.
It output the words where all words that are anagrams, one of the
other, will be at the same line.

It gets one mandatory command line argument: word file path.
"""

import sys
from collections import defaultdict

sorted_words = defaultdict(list)
try:
    with open(sys.argv[1], 'r', encoding='UTF=8') as f:
        for line in f:
            sorted_words[''.join(sorted(list(line.rstrip())))].append(line.rstrip())
except FileNotFoundError as e:
    sys.exit(f'Failed to read words file - {e}\nAborting.')
except IndexError as e:
    sys.exit('ERROR: Missing mandatory command line argument for words-file path.')

for sorted_word in sorted_words:
    print(' '.join(sorted_words[sorted_word]))
