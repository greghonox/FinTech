"""
Question 1
    Create a base class with:
    ● Three properties initialized at construction
    ● One empty classmethod
    ● One empty instance method
"""
from datetime import datetime


class Base:
    def __init__(self, name: str, birth_date: datetime, profession: str, tasks: list) -> None:
        self.name = name
        self.birth_date = birth_date
        self.profession = profession
        self.tasks = tasks

    @classmethod
    def method_class(cls) -> None:
        ...

    def method_instance(self) -> None:
        ...


if __name__ == '__main__':
    name = 'Diogenes'
    birth_date = datetime(1987, 12, 24)
    profession = 'software engineer'
    tasks = ['sleep', 'developer', 'eat']
    test = Base(name, birth_date, profession, tasks)

    print(test.name)
    print(test.birth_date)
    print(test.profession)
    print(test.tasks)

    Base.method_class()
    test.method_instance()
