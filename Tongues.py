#!/usr/bin/python

from random import randint
import re, sys, getopt

the_bible = open("bible.txt", "r")

usage_message = 'Usage: Tongues.py -l <length>'

def print_help_and_exit():
    print(usage_message)
    sys.exit()

def check_numbers(input_string):
    return any(char.isdigit() for char in input_string)
    
def main(argv):
    words = the_bible.read().split()

    sentence = ""
    candidate = ""
    sentence += str(randint(0, 25))
    sentence += ":"
    sentence += str(randint(0, 25))
    sentence += " "

    prev_candidate = ""

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
            try:
                for i in range(int(arg)):
                    candidate = words[randint(0, len(words))]
                    while check_numbers(candidate) or prev_candidate == candidate:
                        candidate = words[randint(0, len(words))]
                    sentence += candidate + " "
                    prev_candidate = candidate;
            except:
                print_help_and_exit()
                

    sentence = sentence[:-1]
#    sentence = re.sub(':', '', sentence)
    sentence += "."
    print(sentence.capitalize())
    

if __name__ == "__main__":
    main(sys.argv[1:])
