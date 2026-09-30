#!/bin/python3


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

    HINT:
    See <https://github.com/mikeizbicki/cmc-csci046/issues/472> for a discussion about a common memory management bug that causes the generated word ladders to be too long in some cases.
    '''
    if start_word == end_word:
        return [start_word]

    wordset = set()
    with open(dictionary_file, 'r', encoding='utf-8') as f:
        for line in f:
            wordset.add(line.strip())
    if start_word not in wordset or end_word not in wordset:
        return None

    wordset.remove(start_word)
    stack = [start_word]
    queue = [stack]

    for current_stack in queue:
        top_word = current_stack[-1]
        words_to_remove = []
        for current_word in wordset:
            if _adjacent(current_word, top_word):
                if current_word == end_word:
                    return current_stack + [current_word]

                stack_copy = copy.copy(current_stack)
                stack_copy.append(current_word)
                queue.append(stack_copy)
                words_to_remove.append(current_word)
        for word in words_to_remove:
            wordset.remove(word)


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''
    if not ladder:
        return False
    for i in range((len(ladder)) - 1):
        if not _adjacent(ladder[i], ladder[i + 1]):
            return False
    return True


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    if len(word1) != len(word2):
        return False
    differences = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            differences += 1
            if differences > 1:
                return False
    return differences == 1
