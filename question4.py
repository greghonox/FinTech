"""
Question 4
    Use the next() function to find the first element in a list of dictionaries whose attribute ‘x’ = 5.
    Default to an empty dictionary if not found.
"""


def next(elements: list) -> 'int|dict':
    if elements[0] == 5:
        return elements[0]
    return {}


items_with_correct = [5, 2, 3, 4, 6]
items_without_incorrect = [3, 4, 1, 3, 5]

print(next(items_with_correct))
print(next(items_without_incorrect))
