#!/usr/bin/python2.7

import argparse

def pigify(word):
  consonants = 'bcdfghjklmnpqrstvwxz'
  vowels = 'aeiou'
  suffixlist = []

  if word[0] in vowels:
    pigword = word + 'way'
    return pigword
  elif word[0] in consonants or word[0] == 'y':
    for index,character in enumerate(word):
      if character == 'y' and index == 0:
        suffixlist.append(character)
      elif character in consonants:
        suffixlist.append(character)
      else:
        break
    suffix = ''.join(suffixlist)
    pigword = word.strip(suffix) + suffix + 'ay'
    return pigword

def main(string):
  wordlist = string.split()
  for index,word in enumerate(wordlist):
    pigword = pigify(word.lower())
    wordlist[index] = pigword
  return wordlist

if __name__=="__main__":
  parser = argparse.ArgumentParser(description="Convert a string to pig-latin")
  parser.add_argument("string", help="The string to convert")
  args = parser.parse_args()
  pigstring = main(args.string)
  print ' '.join(pigstring)
