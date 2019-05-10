"""Print anagrams from file

This script gets a text file (UTF-8) with 1 word in each line.
It output the words where all words that are anagrams, one of the
other, will be at the same line.

It gets 2 command line positional arguments:
1st: Mandatory word file path.
2nd: Optional number (integer) of max word for same anagram. [currently supports 2]
"""

import sys


def is_anagram(word1, word2):
    """
    Check if the 2 words given are each others anagram.
    :param word1: 1st word string.
    :param word2: 2nd word string.
    :return: True if they are anagrams, False otherwise.
    """
    sorted_word1 = ''.join(sorted(list(word1)))
    sorted_word2 = ''.join(sorted(list(word2)))
    return True if sorted_word1 == sorted_word2 else False


test_count = 0
words_list = []
try:
    with open(sys.argv[1], 'r', encoding='UTF=8') as f:
        for line in f:
            words_list.append(line.rstrip())
except FileNotFoundError as e:
    print(f'Failed to read words file - {e}\nAborting.')
    exit(1)

for i in range(len(words_list)):
    if '' == words_list[i]:
        continue
    for j in range(i + 1, len(words_list)):
        if '' == words_list[j]:
            continue
        test_count += 1
        if is_anagram(words_list[i], words_list[j]):
            print(words_list[j], end=' ')
            words_list[j] = ''
            # break if got argument that say: no more than 2 words per anagram.
            if 3 <= len(sys.argv) and '2' == sys.argv[2]:
                print('break', end=' ')
                break
    print(words_list[i])

print('test_count:', test_count)
