Solver for NPR 2016-04-10 Sunday Puzzle
=======================================

Puzzle solver program is dedicated to public domain per CC0.
See http://creativecommons.org/publicdomain/zero/1.0/

Puzzle
------

_NPR Puzzle for 2016-04-10_

http://www.npr.org/2016/04/10/473649171/rearrange-the-letters-in-these-names-to-solve-this-puzzle

_Statement:_

Next week's challenge from listener Peter Collins of Ann Arbor, Mich.:
Name something in eight letters that's usually bought in pairs. Change the
second letter to the letter two spaces later in the alphabet, and you'll get
a new word that names something else that's usually bought in pairs. Both
words are plurals. What are they?

Description
-----------

The solver is a python program that uses a brute force approach to solve
the puzzle.  It searches a word list for all 8-letter words that end in the
letter 's'.  I assume the solution words will end in 's' because the puzzle
states that they are plural.

Once those words are found, it goes through each word and substitutes the
second character with the character two places later.  (for example, if
the second letter is 'a', the replacement letter is 'c').  To see if the new
word is a real word, it searches the same word list to see if there is a
match.  If so, then this is a candidate word pair and is printed out.

This produces a small-ish list of words and a human can examine the results
to see if any of the word pairs solve the puzzle.

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
word pairs.  Upon looking at the resulting word pairs, the answer becomes
obvious.

**sneakers : speakers**

* * *
