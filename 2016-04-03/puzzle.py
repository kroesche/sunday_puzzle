#!/usr/local/bin/python
#
# NPR Sunday Puzzle Solver for 2016-04-03 puzzle
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

# initialize word list of all words with 5 letters
words5 = []

def cval(c):
    return 1 + ord(c) - ord('a')

# assume word list is contained in local file words.txt
# go through the all-words list and make list of words with 5 letters
# we can start with words that begin with ord > 5 because it is impossible
# for words that start with any lower letters to be a solution.  The ord
# of the first letter of the solution must be at least 5
# (and we know that is not an answer anyway because that word would be
# 'eaaaa').  This is not a complete optimization but it knocks out a bunch
# of non-candidate words without much effort.
with open('words.txt', 'r') as f:
    for word in f:
        word = word.strip().lower()
        if len(word) == 5:
            if ord(word[0]) > ord('e'):
                words5 += [word]

# go through list of all 5-letter words from above
for w in words5:
    if cval(w[0]) == (cval(w[1]) + cval(w[2]) + cval(w[3]) + cval(w[4])):
        print(w)
