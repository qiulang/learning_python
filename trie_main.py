#! /usr/bin/env python3

from trie4 import Trie

t2 = Trie('foo', 'bar', 'baz', 'barz')
print(t2.in_trie('baz'))
print(t2.in_trie('barzz'))
t3 = Trie("abc", "abcd", "aa", "abbbaba", "abk", "abce")
print(t3)
t3.suggestion("abc")
