#!/usr/bin/env python3

from spellchecker import SpellChecker
spell = SpellChecker()

def banner():
    print('''
                                _ _ ______                     _                 
                               | | |  ____|                   (_)                
                 ___ _ __   ___| | | |__  __  ____ _ _ __ ___  _ _ __   ___ _ __ 
                / __| '_ \ / _ \ | |  __| \ \/ / _` | '_ ` _ \| | '_ \ / _ \ '__|
                \__ \ |_) |  __/ | | |____ >  < (_| | | | | | | | | | |  __/ |   
                |___/ .__/ \___|_|_|______/_/\_\__,_|_| |_| |_|_|_| |_|\___|_|   
                    | |                                                          
                    |_|                         Handcoded By: Satan101
            ''')

def wordSeparator(suspectList):
    for phrase in suspectList:
        wordList = phrase.split(' ')
        for word in wordList:
            if word.endswith('.') or word.endswith('!') or word.endswith('?') or word.endswith(',') or word.endswith(':') or word.endswith('-') or word.endswith('='):
                newWord = word.replace(word[-1],'')                 #newWord is the modified word
                examiner(newWord)
            elif word is '' or word is '\n':
                pass
            else:
                examiner(word)

def examiner(word):
    if word in spell:
        pass
    else:
        print('The word: "' +word+ '" seems to be incorrect. The most likely suggestion is "' +spell.correction(word)+ '"')


def mainF():

    banner()

    with open(input('Enter a file to check: '), 'r') as suspect:
        contents = suspect.read()

    suspectList = contents.splitlines()

    wordSeparator(suspectList)

mainF()
