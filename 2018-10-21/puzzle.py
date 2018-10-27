#!/usr/local/bin/python
#
# NPR Sunday Puzzle Solver for 2018-10-21 puzzle
#
# Written in 2018 by Joseph Kroesche joe@kroesche.org
#
# To the extent possible under law, the author(s) have dedicated all
# copyright and related and neighboring rights to this software to the
# public domain worldwide. This software is distributed without any warranty.
#
# This is a CC0 Public Domain Dedication.  For more information, see
# <http://creativecommons.org/publicdomain/zero/1.0/>.
#

from __future__ import print_function
from itertools import permutations

# initialize original list of characters
input_list = ['b', 'e', 'e', 'r', 'm', 'o', 'u', 't', 'h']

# initialize word list of all words with 3 letters
words3 = []

# assume word list is contained in local file words.txt
# go through the all-words list and make list of words with 3 letters
with open('words.txt', 'r') as f:
    for word in f:
        word = word.strip().lower()
        if len(word) == 3:
            words3 += [word]

# now words3 contains all the 3 letter words in the dictionary

# return 3 letter word at the specified row (0-2)
def row_word(thelist, row_num):
    starti = row_num * 3
    return ''.join(thelist[starti:starti+3])

# return 3 letter word at the specified column (0-2)
def col_word(thelist, col_num):
    word3 = []
    for idx in range(col_num, col_num + 7, 3):
        word3.append(thelist[idx])
    return ''.join(word3)

# return 3 letter word of the diagonal (0-1)
def diag_word(thelist, diag_num):
    word3 = []
    adder = 4 if diag_num == 0 else 2
    start = 0 if diag_num == 0 else 2
    stop = 9 if diag_num == 0 else 7
    for idx in range(start, stop, adder):
        word3.append(thelist[idx])
    return ''.join(word3)

# get all the permutations of the input list
perms = permutations(input_list)

# iterate over all permutations and test for valid words in the matrix
# check each of 3 rows, each of 3 columns, and the two diagonals
# if all of these are valid 3 letter words, then the permutation is a
# possible solution
for perm in perms:
    failed = False
    for row in range(3):
        wrd = row_word(perm, row)
        if not wrd in words3:
            failed = True
            break
    if failed:
        continue
    for col in range(3):
        wrd = col_word(perm, col)
        if not wrd in words3:
            failed = True
            break
    if failed:
        continue
    for diag in range(2):
        wrd = diag_word(perm, diag)
        if not wrd in words3:
            failed = True
            break
    if failed:
        continue

    # getting here means all the tests are valid words
    # print the 3x3 array
    print("===")
    for row in range(3):
        print(row_word(perm, row))
    print("---")
