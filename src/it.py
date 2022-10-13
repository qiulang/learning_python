import itertools
import operator

robots = [
    {"name": "blaster", "faction": "autobot"},
    {"name": "galvatron", "faction": "decepticon"},
    {"name": "jazz", "faction": "autobot"},
    {"name": "metroplex", "faction": "autobot"},
    {"name": "megatron", "faction": "decepticon"},
    {"name": "starcream", "faction": "decepticon"},
]
sort_key = lambda k: k['faction']
# key specifies a function of one argument that is used to extract a comparison key from each element in iterable
for key, group in itertools.groupby(sorted(robots,key = sort_key), key=sort_key):
    print(f"{key}:{list(group)}")

data = [{'name': 'Alan', 'age': 34},
        {'name': 'Betsy', 'age': 29},
        {'name': 'David', 'age': 33},
        {'name': 'Catherine', 'age': 34},]
sort_key = lambda k: k['age']
grouped_data = itertools.groupby(sorted(data,key=sort_key), key=sort_key)
for key, grp in grouped_data:
    print(f"{key}:{list(grp)}")