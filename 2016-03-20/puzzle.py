#!/usr/local/bin/python
#
# NPR Sunday Puzzle Solver for 2016-03-20 puzzle
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
import re

# regex to find word with 5 consecutive consonants
cons5_regx = re.compile('^(.*)[bcdfghjklmnpqrstvwxz]{5}(.*)$')

# regex to find 3 vowels
vowel3_regx = re.compile('.*[aeiouy]{3}.*')

# initialize word list of all words with 9 letters
words9 = []

# assume word list is contained in local file words.txt
# go through the all-words list and make list of words with 9 letters
with open('words.txt', 'r') as f:
    for word in f:
        word = word.strip().lower()
        if len(word) == 9:
            words9 += [word]

# go through list of all 9-letter words
for word in words9:
    # find words that have 5 consecutive consonants
    m = re.match(cons5_regx, word)
    if m:
        print("%s: %s-----%s:" % (word, m.group(1), m.group(2)), end='')

        # create a new regex out of the found word in order to find all other
        # words with same pattern outside of the 5-consonant section of the
        # word
        new_regx = re.compile("^%s([a-zA-Z]{5})%s$" % (m.group(1), m.group(2)))

        # go through list of all 9-letter words to find any that could
        # have a common matching with our 5-consonant word
        for newword in words9:
            newm = re.match(new_regx, newword)
            if newm:
                # found a word that can match
                # check to see if the replaced section has 3 vowels
                vm = re.match(vowel3_regx, newm.group(1))
                if vm:
                    print(' ', newword, end='')
        print('\n')
