#!/usr/bin/env python
# Usage: echo Hello world | ./morse.py

import sys

# our distionary used for mapping characters to morse code
morse = {
         # international morse code table
            # characters
         'a':'.-',    'b':'-...',  'c':'-.-.',  'd':'-..',   'e':'.',
         'f':'..-.',  'g':'--.',   'h':'....',  'i':'..',    'j':'.---',
         'k':'-.-',   'l':'.-..' , 'm':'--',    'n':'-.',    'o':'---',
         'p':'.--.',  'q':'--.-',  'r':'.-.',   's':'...',   't':'-',
         'u':'..-',   'v':'...-',  'w':'.--',   'x':'-..-',  'y':'-.--',
         'z':'--..',
            # numbers
         '0':'-----', '1':'.----', '2':'..---', '3':'...--', '4':'....-',
         '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.',
         # special case: word spacing
         ' ':''
         }

def translate(string):
    out = ''
    err = 0
    string = string.lower()
    for char in string:
        try:
            out = out + morse[char] + '/'
        except:
            # ignore newlines
            if char != '\n':
                sys.stderr.write("Invalid input: '" + char + "'\n")
                err += 1
    # cut the last '/' (letter spacing) of the string before return
    return out[:-1], err


# --- Main ---
out = ''
err = 0
inp = sys.stdin.readlines()
if inp:
    for i in inp:
        out, err = translate(i)
        print out

sys.exit(err)
