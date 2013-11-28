import sys
import json
import random

def format_output(*words):
    result = []
    for word in words:
        if word[0] == "-":
            if not len(result):
                result.append(word[1:].capitalize())
            else:
                result.append(word)
        else:
            result.append(word.capitalize())
    result = " ".join(result).replace(" -", "")
    return result

def fill_dictionary(path):
    words = {letter: set() for letter in backronym_string}
    with open(path) as f:
        for line in f:
            if line[0] == "#":
                continue
            for word in line.split():
                letter = word[0]
                if word[0] == "-":
                    letter = word[1]
                words[letter.capitalize()].add(word)
    return words

def randomize(*iterables):
    chosen = []
    for iterable in iterables:
        chosen.append(random.choice(list(iterable)))
    return chosen

def read_config(path):
    with open(path) as f:
        # return first line, without \n at the end
        backronym_string = f.readline()[:-1]
        dictionary_path = f.readline()[:-1]
        return (backronym_string, dictionary_path)

try:
    backronym_string, dict_path = read_config("config.me")
    words = fill_dictionary(dict_path)
    randomized = randomize(*[words[letter] for letter in backronym_string])
    print json.dumps(format_output(*randomized))
except IOError as e:
    print str(e)
    print "Make sure config.me resides in the same directory as " + __file__
    print "And that the second line in config.me contains the dictionary path"
