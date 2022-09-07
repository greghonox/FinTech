"""
Question 2
    Create a derived class from the base class
    ● Inherits all properties and methods from the base class
    ● Initialize the properties differently from the base class
    ● Add code to the empty methods
"""
from datetime import datetime
from question1 import Base


class Derived(Base):
    def __init__(self, name: str, birth_date: datetime, profession: str, tasks: list) -> None:
        super().__init__(name, birth_date, profession, tasks)

    def get_name(self) -> None:
        ...

    def get_birth_date(self) -> None:
        ...


if __name__ == '__main__':
    name = 'Diogenes'
    birth_date = datetime(1987, 12, 24)
    profession = 'software engineer'
    tasks = ['sleep', 'developer', 'eat']
    test = Derived(name, birth_date, profession, tasks)

    print(test.name)
    print(test.birth_date)
    print(test.profession)
    print(test.tasks)

    test.method_instance()
    test.get_birth_date()
    test.get_name()
