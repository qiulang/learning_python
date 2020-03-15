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


print(in_trie(make_trie('foo', 'bar', 'baz', 'barz'), 'baz'))
print(in_trie(make_trie('foo', 'bar', 'baz', 'barz'), 'barz'))
print(in_trie(make_trie('foo', 'bar', 'baz', 'barz'), 'barzz'))
print(in_trie(make_trie('foo', 'bar', 'baz', 'barz'), 'bart'))
print(in_trie(make_trie('foo', 'bar', 'baz', 'barz'), 'ba'))
