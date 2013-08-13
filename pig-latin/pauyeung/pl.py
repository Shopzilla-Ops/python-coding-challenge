#!/bin/python

vowels = ("a", "A", "e", "E", "i", "I", "o", "O", "u", "U")

sentence = raw_input("Enter your sentence: ")

words = sentence.split()

for character in words:
    if character[0] in vowels:
        print character + "way",
    else:
        print character[1:] + character[0] + "ay",
