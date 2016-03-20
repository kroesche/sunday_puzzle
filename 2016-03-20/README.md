Solver for NPR 2016-03-20 Sunday Puzzle
=======================================

Puzzle solver program is dedicated to public domain per CC0.
See http://creativecommons.org/publicdomain/zero/1.0/

Puzzle
------

_NPR Puzzle for 2016-03-20_

http://www.npr.org/2016/03/20/471102829/first-and-last-two-letters-are-key-to-solve-this-puzzle-thats-not-so-easy

_Statement:_

Next week's challenge, from listener Andrew Chaikin of San Francisco:
Think of a common nine-letter word that contains five consecutive consonants.
Take three consecutive consonants out of these five and replace them with
vowels to form another common nine-letter word. What is it?

Description
-----------

The solver is a python program that uses a brute force approach to solve
the puzzle.  It searches a word list for all 9-letter words that have
5 consecutive consonants.  It assumes _y_ is a consonant.

Once those words are found, makes a new matching pattern out of the parts
of the word that are not the 5-consonant section of the word.  It then finds
all words that match that new pattern.  For example, the word _synthetic_
has 5 consonants at the beginning of the word.  So the new matching pattern
is _-----etic_.  It then searches for all words that end in _-etic_.

For words that match the new pattern, they are checked for 3 consecutive
vowels in the 5-letter section that was substituted.  If that is true
then the word pair (original word and new word) is a solution to the puzzle.

To use the program you need a file that contains a word list, one word per
line.  The name of the file should be words.txt.

Word lists
----------

There are a number of words lists available by doing a google search.  The
first word list to use is the built in word list on your computer, found
in `/usr/share/dict/words`.  This list has 250000+ words.  However using this
list I got no solution.  I then found another word list here:

https://github.com/dwyl/english-words

This has about 350000+ words.  Using this list I found one solution.

I also found a couple of other word lists, although these were not as
handy because all the words were not in just one big list.

http://wordlist.aspell.net  
http://dreamsteep.com/projects/the-english-open-word-list.html

Solution
--------

Using the above word list I found only one solution:

**strengths : strenuous**

* * *
