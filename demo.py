import numpy as np

# List
spam = ["cat", "bat", "rat", "elephant"]
spam.sort()
print("spam list", spam)


# condition
hour = 14

if hour < 8:  # if hour is less than 8
    print("It's morning")
elif hour < 18:  # if hour is beetween 8 and 18
    print("It's the day")
else:  # if hour is upper than 18
    print("It's the evening")


# numpy
arr = np.linspace(0, 15, 16)
print(arr)

# function
def add(*b):
    c = 0
    for i in b:
        c = c + i
    return c


addvalue = add(2, 4, 5, 6)
print("Added value", addvalue)  # Added value 17

# Filter map and reduce

mylist = [5, 4, 6, "other random stuff", True, "22", "map", False, ""]


def multiply_by_two(obj):
    return obj * 2


def is_str(obj):
    return type(obj) == str


list(map(multiply_by_two, mylist))
# [10, 8, 12, "other random stuffother random stuff", 2, "2222", "mapmap", 0, ""]

list(filter(is_str, mylist))
# ["other random stuff", "22", "map", ""]

# You could also use lambdas on both examples:
list(map(lambda x: x * 2, mylist))
list(filter(lambda x: type(x) == str, mylist))
