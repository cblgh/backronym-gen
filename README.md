#Backronym Generator


Generates a backronym from a specified dictionary file. The backronym is generated as a valid json string via stdout.


####The config file
The first line in `config.me` is the acronym you want to generate a backronym for.  
The second line is the path of the dictionary file, from which you will generate the backronym.

####The dictionary file
`#` at the start of a line is a comment, and will be skipped  
`-` prepended to a word means that it will be added to the word before it
e.g. lund hacker -space will yield Lund Hackerspace

Otherwise just pump the dictionary full with words that start with the same letter as one of the acronym's!

#### Usage
`python2.7 backronym-gen.py`

This project is licensed under the terms of the MIT license.
