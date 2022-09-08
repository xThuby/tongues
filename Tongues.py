#!/usr/bin/python

import numpy as np
from random import randint
import re, sys, getopt

usage_message = 'Usage: Tongues.py -l <length>'

def print_help_and_exit():
    print(usage_message)
    sys.exit()

def check_numbers(input_string):
    return any(char.isdigit() for char in input_string)

def make_pairs(corpus):
    for i in range(len(corpus)-1):
        yield (corpus[i], corpus[i+1])
    
def main(argv):

    try:
        opts, args = getopt.getopt(argv, "hl:", ["length="])
    except getopt.GetoptError:
        print_help_and_exit()

    if len(opts) == 0:
        print_help_and_exit()
        

    for opt, arg in opts:
        if opt == '-h':
            print_help_and_exit()
        elif opt in ("-l", "--length"):
            generate_bible_verse(int(arg))
        else:
            print_help_and_exit()

def generate_bible_verse(length):
    # Start with random chapter and verse

    corpus = open("bible.txt", "r").read().split()

    pairs = make_pairs(corpus)

    word_dict = {}
    for word_1, word_2 in pairs:
        if word_1 in word_dict.keys():
            word_dict[word_1].append(word_2)
        else:
            word_dict[word_1] = [word_2]

    first_word = np.random.choice(corpus)

    verse = str(randint(1, 25))
    verse += ":"
    verse += str(randint(1, 25))

    chain = [verse, first_word]

    for i in range(length):
        chain.append(np.random.choice(word_dict[chain[-1]]))

    print(' '.join(chain))



if __name__ == "__main__":
    main(sys.argv[1:])
