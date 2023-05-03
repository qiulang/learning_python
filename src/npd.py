from collections import namedtuple

NamedTupleCard = namedtuple('NamedTupleCard', ['rank', 'suit'])
queen_of_hearts = NamedTupleCard('Q', 'Hearts')
print(queen_of_hearts == ('Q', 'Hearts'))
print(queen_of_hearts.rank)