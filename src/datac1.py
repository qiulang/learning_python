from dataclasses import dataclass, field


# @dataclass
# class Team:
#     name: str
#     # members: list = field(default_factory=list)
#     members: list = []


# # Let's see what's really happening
# print(id(Team.__dataclass_fields__['members'].default))  # Some memory address

# team1 = Team("A")
# team2 = Team("B")

# print(id(team1.members))  # SAME memory address!
# print(id(team2.members))  # SAME memory address!

# # They literally point to the same list object
# print(team1.members is team2.members)  # True

class Team:
    def __init__(self, name, members=[]):  # Still dangerous!
        self.name = name
        self.members = members


team1 = Team("A")
team2 = Team("B")
team1.members.append("Alice")
print(team2.members)  # ['Alice'] - shared!


def add_item(item, my_list=[]):  # Default evaluated once at function definition
    my_list.append(item)
    return my_list


print(add_item(1))  # [1]
print(add_item(2))  # [1, 2] - Wait, what?!
print(add_item(3))  # [1, 2, 3] - The list persists!


@dataclass
class Bad:
    x: int = 1
    y: int
