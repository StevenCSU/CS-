# madLibs.py - Change the word you want to replace.

import sys

# open the file
filename = sys.argv[1]  
resultName = filename + '-result'
resultContent = ''
with open(filename) as f:
    content = f.readlines()
    for line in content:
        l = line.split()
        # replace the word
        for i in range(len(l)):
            if l[i] == 'ADJECTIVE' or l[i] == 'ADJECTIVE.':
                adj = input('Enter an adjective:\n')
                l[i] = adj
            elif l[i] == 'NOUN' or l[i] == 'NOUN.':
                noun = input('Enter a noun:\n')
                l[i] = noun
            elif l[i] == 'VERB' or l[i] == 'VERB.':
                verb = input('Enter a verb:\n')
                l[i] = verb
            elif l[i] == 'ADVERB' or l[i] == 'ADVERB.':
                adverb = input('Enter an adverb:\n')
                l[i] = adverb
        resultLine = ' '.join(l)
        resultContent += resultLine

# write into a new text
with open(resultName, 'w') as r:
    r.write(resultContent)
    print('The result content is: \n')
    print(resultContent)


