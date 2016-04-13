Solver for NPR 2016-04-03 Sunday Puzzle
=======================================

Puzzle solver program is dedicated to public domain per CC0.
See http://creativecommons.org/publicdomain/zero/1.0/

Puzzle
------

_NPR Puzzle for 2016-04-03_

http://www.npr.org/2016/04/03/472825113/got-2-words-in-the-same-category-its-rhymin-time

_Statement:_

Next week's challenge: Take the word EASY:
Its first three letters — E, A and S — are the fifth, first, and nineteenth
letters, respectively, in the alphabet. If you add 5 + 1 + 19, you get 25,
which is the value of the alphabetical position of Y, the last letter of
EASY.

Can you think of a common five-letter word that works in the opposite
way — in which the value of the alphabetical positions of its last four
letters add up to the value of the alphabetical position of its first
letter?

Description
-----------

The solver is a python program that uses a brute force approach to solve
the puzzle.  It searches a word list for all 5-letter words that start with
'e' or any later letter.  Because of the alphabet math described in the
puzzle statement, it is not possible for any solution words to start with
any letter sooner than 'e' (and probably later than that).

Once it has the 5-letter word list, it simply does the calculation listed
in the puzzle statement for each word, and prints it if it satisfies the
alphabet math in the puzzle.

To use the program you need a file that contains a word list, one word per
line.  The name of the file should be words.txt.

Word lists
----------

There are a number of words lists available by doing a google search.  The
first word list to use is the built in word list on your computer, found
in `/usr/share/dict/words`.  This list has 250000+ words.

I found another word list here:

https://github.com/dwyl/english-words

This has about 350000+ words.  This is the list I used to solve the puzzle.

I also found a couple of other word lists, although these were not as
handy because all the words were not in just one big list.

http://wordlist.aspell.net  
http://dreamsteep.com/projects/the-english-open-word-list.html

Solution
--------

Using the method described above, the python program produces about 20
words, some of which don't make much sense.  Here are some of the solution
words that make sense:

**table, whack, zebra**

* * *
