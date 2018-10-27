Solver for NPR 2018-10-21 Sunday Puzzle
=======================================

Puzzle solver program is dedicated to public domain per CC0.
See http://creativecommons.org/publicdomain/zero/1.0/

Puzzle
------

_NPR Puzzle for 2018-10-21_

https://www.npr.org/2018/10/21/659245659/sunday-puzzle-find-the-missing-link

_Statement:_

**Next week's challenge:** Take the 9 letters of BEER MOUTH. Arrange them in a
3x3 array so that the three lines Across, three lines Down, and both diagonals
spell common 3-letter words. Can you do it?

Description
-----------

The solver is a python program that uses a brute force approach to solve the
puzzle. It creates a 3X3 array from the 9 characters of BEER MOUTH. It checks
that all 3 rows and columns and two diagonals have 3 letter words that appear
in the dictionary or word list. It tests all possible permutations and prints
out every permutation that satisfies the test.

The results list is examined by a human to determine which is the most likely
correct answer.

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

Using the method described above, the python program produces only one
solution. It prints it twice because the algorithm does not consider that the
two E's are the same character and so it does an extra test that is not really
needed.

The solution is:

    ===
    orb
    hue
    met
    ---

* * *
