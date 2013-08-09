#!/usr/bin/python2.7

import argparse


class Translation(object):
    '''This object provides various translations for a given phrase'''
    def __init__(self, phrase, native='en'):
        self.phrase = phrase

    @property
    def pig_latin(self):
        VOWELS = tuple(list('aeiou'))
        for token in self.phrase.split():
            print token
            if not token:
                continue
            elif not token.isalpha:
                yield token
            elif token.lower().startswith(VOWELS):
                yield ''.join([token, 'way'])
            elif not token.lower().startswith(VOWELS):
                vowel_pos_list = [token.lower().find(v) for
                                  v in VOWELS if
                                  token.find(v) != -1]
                if not vowel_pos_list:
                    yield token
                else:
                    first_vowel_pos = min(vowel_pos_list)
                    yield ''.join([
                        token[first_vowel_pos:],
                        token[:first_vowel_pos],
                        'ay'
                    ])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('language', help='language to translate into',
                        choices=['platin'])
    parser.add_argument('phrase', help='phrase to translate')
    args = parser.parse_args()
    phrase = Translation(args.phrase)
    handlers = {
        'platin': phrase.pig_latin,
    }
    print '\n', ' '.join(list(handlers.get(args.language)))
