#!/usr/local/bin/python
#
# NPR Sunday Puzzle Solver for 2016-04-10 puzzle
#
# Written in 2016 by Joseph Kroesche joe@kroesche.org
#
# To the extent possible under law, the author(s) have dedicated all
# copyright and related and neighboring rights to this software to the
# public domain worldwide. This software is distributed without any warranty.
#
# This is a CC0 Public Domain Dedication.  For more information, see
# <http://creativecommons.org/publicdomain/zero/1.0/>.
#

from __future__ import print_function

# initialize word list of all words with 8 letters
words8 = []

# assume word list is contained in local file words.txt
# go through the all-words list and make list of words with 8 letters
# assume all candidates end in 's'
with open('words.txt', 'r') as f:
    for word in f:
        word = word.strip().lower()
        if len(word) == 8:
            if word[7] == 's':
                words8 += [word]

# go through list of all 8-letter words from above
for word in words8:
    # change the second char to charval+2
    char2 = word[1]
    char2 = chr(ord(char2) + 2)
    tryword = word[:1] + char2 + word[2:]

    # see if the new word is in the word list
    for newword in words8:
        if tryword == newword:
            print(word, ':', tryword, '\n')
            break
