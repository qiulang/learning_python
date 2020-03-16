#! /usr/bin/env python3
from collections import defaultdict

# s = 'mississippi'
# d = defaultdict(int)
# for k in s:
#     d[k] += 1

# print(d.items())

# s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# d = defaultdict(list)
# for k, v in s:
#     d[k].append(v)

# print(d.items())

_end = '_end_'


def make_trie(*words):
    root = {}
    # root = defaultdict(dict)
    for word in words:
        current_dict = root
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})
            # current_dict = current_dict[letter]
        current_dict[_end] = _end
    return root


trie = make_trie(('foo', 'bar', 'baz', 'barz',))
print(trie)

# print(in_trie(make_trie('foo', 'bar', 'baz', 'barz'), 'baz'))
# print(in_trie(make_trie('foo', 'bar', 'baz', 'barz'), 'barz'))
# print(in_trie(make_trie('foo', 'bar', 'baz', 'barz'), 'barzz'))
# print(in_trie(make_trie('foo', 'bar', 'baz', 'barz'), 'bart'))
# print(in_trie(make_trie('foo', 'bar', 'baz', 'barz'), 'ba'))


def in_trie(trie, word):
    current_dict = trie
    for letter in word:
        if letter not in current_dict:
            return False
        current_dict = current_dict[letter]
    print('final check for leaf')
    return _end in current_dict


def suggestion(trie, prefix):
    curr = trie
    for letter in prefix:
        if letter not in curr:
            return ''
        curr = curr[letter]
    # print('final check for remaining leaf')
    if _end in curr:
        return ''
    result = dfirst(curr, prefix)
    print("recursive function is always a headache")
    print(result)


def dfirst(start, prefix):
    for key in start:
        next = start[key]
        if next == _end:
            print(prefix)
        else:
            word = prefix + key
            dfirst(next, word)
    return prefix  # 可以没有

# 对比


def dfirst2(start, prefix):
    for key in start:
        next = start[key]
        if next != _end:
            word = prefix + key
            dfirst2(next, word)
    print(prefix)
    return prefix


root = make_trie("abc", "abcd", "aa", "abbbaba", "abk")
print(root)
print(f'store "abc", "abcd", "aa", "abbbaba" and find prefix "ab"')
suggestion(root, "ab")
