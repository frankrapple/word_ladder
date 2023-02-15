#!/bin/python3

from collections import deque

import copy


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''
    if start_word == end_word:
        return [start_word]

    stack = [start_word]
    queue = [stack]
    dictionary_file = open(dictionary_file).read().split()

    while queue:
        curr_stack = queue.pop(0)
        curr_word = curr_stack[-1]

        for word in dictionary_file:
            if _adjacent(curr_word, word):
                if word == end_word:
                    curr_stack.append(word)
                    return curr_stack
                else:
                    copy_stack = curr_stack.copy()
                    copy_stack.append(word)
                    queue.append(copy_stack)
                    dictionary_file.remove(word)

    return None

def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''
    if ladder == None:
        return False

    if len(ladder) == 0:
        return False
	
    count = 0
    
    for i in range(len(ladder) - 1):
        if ladder[i] == ladder[i+1]:
            return False
        B = _adjacent(ladder[i], ladder[i+1])
        if B == True:
            count += 1
    if count == (len(ladder) - 1):
        return True
    else:
        return False

def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''

    if word1 == word2:
        return False
    if len(word1) != len(word2):
        return False
    count = 0
    index = 0
    while index<len(word1) and index<len(word1):
        for i in word1:
            if word1[index] != word2[index]:
                count += 1
            index +=1
        if count == 1:
            return(True)
        else:
            return(False)
