## Pig Latin - Pig Latin is a game of alterations played on the English language game. 
## To create the Pig Latin form of an English word the initial consonant sound is 
## transposed to the end of the word and an ay is affixed (Ex.: "banana" would yield anana-bay). 
## Read Wikipedia for more information on rules.
## 
## https://en.wikipedia.org/wiki/Pig_Latin
## 
## For words that begin with consonant sounds, the initial consonant or consonant cluster 
## is moved to the end of the word, and "ay" is added, as in the following examples:
## 
##     "happy" -> "appyhay"
##     "duck" -> "uckday"
##     "glove" -> "oveglay"
## 
## For words that begin with vowel sounds or silent letter, "way" is added at the end of the word. Examples are
## 
##     "egg" -> "eggway"
##     "inbox" -> "inboxway"
##     "eight" -> "eightway"
## 
## The letter 'y' can play the role of either consonant or vowel, depending on its location
## 
##     "yellow" -> "ellowyay"
##     "rhythm" -> "ythmray"

import sys

# Global for vowels
vowels = ["a","e","i","o","u"]

class myword:

    # Set the word in the class
    def __init__(self, theword):
        self.word = theword.lower()

    # Check if the first letter is a vowel
    def isFirstVowel(self):
        letter = self.word[0]
        if letter in vowels:
            return True
        return False

    # Make the word pig latin
    def latinize(self):
        if self.isFirstVowel():
            # Add "way" to the end - this is easy
            self.word = self.word + "way"
        else:
            # We know the first letter is not a vowel, throw it on the end
            end = self.word[0]
            self.word = self.word[1:]
            # Find he first vowel and go from there
            for letter in self.word:
                if letter in vowels or letter == "y":
                    # Got a vowel
                    self.word = self.word + end + "ay"
                    return self.word
                # No vowel yet, keep looking
                end = end + self.word[0]
                self.word = self.word[1:]
        return self.word


if __name__ == '__main__':
    sentence = ""

    # Go through each word, but make sure it is an actual word
    for w in  sys.argv[1:]:
        if w.isalpha():
            pig = myword(w)
            sentence = sentence + " " + pig.latinize()
        else:
            sentence = sentence + " " + w

    # Print the final product
    print sentence
