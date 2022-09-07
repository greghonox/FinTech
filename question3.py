"""
Question 3
    Use list comprehension and a lambda function to extract all of the even integers out of a list of
    integers
"""

tasks_generic = ['run', 'build', 'sleep', 'eat', 2, 3, 100, 290, 7]


f = lambda x: x if isinstance(x, int) and x % 2 == 0 else None


[print(item) for item in tasks_generic if f(item)]
