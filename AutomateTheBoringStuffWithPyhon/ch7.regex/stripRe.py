# stripRe.py - The Regex version of python function strip()

import re

def stripRe(string, word=' '):
    """
    remove the space around the string(front and after)
    if word is not space, remove the word in the string
    """
    if word == ' ':
        spaceRegex = re.compile(r'^ | $')
        return spaceRegex.sub('', string)
    else:
        wordRegex = re.compile(r'' + str(word) + r'')
        return wordRegex.sub('', string)

s = ['hello W ', '  Hello world', ' hello World  ']
for i in range(len(s)):
    print(stripRe(s[i], 'l'))


# TODO: version for use.
# s = input('Please input the sentence first: ')
# print('Please input the word you want to remove: ')
# w = input('if')
