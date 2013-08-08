'''
 Pig Latin - Pig Latin is a game of alterations played on the English language game. 
 To create the Pig Latin form of an English word the initial consonant sound is 
 transposed to the end of the word and an ay is affixed (Ex.: "banana" would yield anana-bay). 
 Read Wikipedia for more information on rules.
 
 https://en.wikipedia.org/wiki/Pig_Latin
 
 For words that begin with consonant sounds, the initial consonant or consonant cluster 
 is moved to the end of the word, and "ay" is added, as in the following examples:
 
     "happy" -> "appyhay"
     "duck" -> "uckday"
     "glove" -> "oveglay"
 
 For words that begin with vowel sounds or silent letter, "way" is added at the end of the word. Examples are
 
     "egg" -> "eggway"
     "inbox" -> "inboxway"
     "eight" -> "eightway"
 
 The letter 'y' can play the role of either consonant or vowel, depending on its location
 
     "yellow" -> "ellowyay"
     "rhythm" -> "ythmray"
'''

import sys
import re

''' Global for vowels '''
vowels = ["a","e","i","o","u"]

class myword:

    ''' Set the word in the class '''
    def __init__(self, word):
        self.word = word.lower()

        self.setPunct()

        ''' Set a flag if this is actually a word '''
        self.alpha = True
        if not self.word.isalpha():
            self.alpha = False

    def setPunct(self):
        ''' If ending punctuation strip and save for later'''
        pattern = "(\.|,|\?|:|;|!)$"
        result = re.search(pattern, self.word)
        if result:
            self.punct = result.group(0)
            self.word = self.word[:-1]
        else:
            self.punct = False

    ''' Check if the first letter is a vowel '''
    def isFirstVowel(self):
        letter = self.word[0]
        if letter in vowels:
            return True
        return False

    ''' Make the word pig latin '''
    def latinize(self):
        ''' If this is not a true word, just give it back '''
        if not self.alpha:
            return self.word

        ''' If the word starts with a vowel, Add "way" to the end - this is easy '''
        if self.isFirstVowel():
            self.latin = self.word + "way"
        else:
            ''' We know the first letter is not a vowel, throw it on the end '''
            end = self.word[0]
            self.latin = self.word[1:]
            ''' Find he first vowel and go from there '''
            for letter in self.latin:
                if letter in vowels or letter == "y":
                    ''' Got a vowel '''
                    self.latin = self.latin + end + "ay"
                    return self.latin
                ''' No vowel yet, keep looking '''
                end = end + self.latin[0]
                self.latin = self.latin[1:]
        return self.latin

    def isPalindrome(self):
        ''' If this is not a true word, just give it back '''
        length = len(self.word)
        if not self.alpha or length == 1:
            return False

        pal = self.word
        half = length / 2
        if length % 2:
            ''' Remove the middle letter '''
            pal = pal[0:half] + pal[half+1:]
        ''' Take the first half, then reverse the second half and compare '''
        first = pal[half:]
        second = pal[:half]
        second = second[::-1]
        if first == second:
            return True
        else:
            return False

def help(string):
    print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    print "It's pretty simple, just give me a bunch of words"
    print "No special arguements, no spaces, nothing like that"
    print "Maybe you need an example?"
    print
    print "\tpython iglatinpay.py this is a great example"
    print
    print "Now, let's take a minute and marvel at the above example"
    print "No spaces, no dashes, no funny stuff.  Now knock it off and let's get going!!!"
    print 'This: "' + string + '" is not helping'
    sys.exit(1)

if __name__ == '__main__':
    sentence = ""
    sentence2 = ""

    count = 0
    ''' Go through each word, but make sure it is an actual word '''
    for word in  sys.argv[1:]:
        if ' ' in word or '-' in word:
            help(word)
        pig = myword(word)
        sentence = sentence + " " + pig.latinize()
        ''' Add punctuation back in '''
        if pig.punct:
            sentence = sentence + pig.punct
        if pig.isPalindrome():
            count += 1

    ''' Print the final product '''
    print sentence
    if count:
        print "Oh, by the way, there were " + str(count) + " palindromes in that sentence"

