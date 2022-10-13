#! /usr/bin/env python3
from collections import defaultdict


# def _trie(): return defaultdict(_trie)
#_trie = lambda: defaultdict(_trie) # noqa
def _trie(): return defaultdict(_trie)


_end = '_end_'


def make_trie(*words):
    root = _trie()
    for word in words:
        current_dict = root
        for letter in word:
            current_dict = current_dict[letter]
        current_dict[_end] = _end
    return root


def in_trie(trie, word):
    curr = trie
    for w in word:
        if w not in curr:
            return False
        curr = curr[w]
    print('final check for leaf')
    return _end in curr


def suggestion(trie, prefix):
    curr = trie
    for letter in prefix:
        if letter not in curr:
            return ''
        curr = curr[letter]
    print('final check for remaining leaf')
    if _end in curr:
        return ''
    dfirst(curr, prefix)


def dfirst(start, word):
    if (_end in start):
        return word
    for key in start:
        next = start[key]
        prefix = word+key
        w = dfirst(next, prefix)
        print(w)


# print(in_trie(make_trie('foo', 'bar', 'baz', 'barz'), 'baz'))
# print(in_trie(make_trie('foo', 'bar', 'baz', 'barz'), 'barz'))
# print(in_trie(make_trie('foo', 'bar', 'baz', 'barz'), 'barzz'))
# print(in_trie(make_trie('foo', 'bar', 'baz', 'barz'), 'bart'))
# print(in_trie(make_trie('foo', 'bar', 'baz', 'barz'), 'ba'))

root = make_trie(("abc", "abcd", "aa", "abbbaba",))
suggestion(root, "ab")
