from functools import partial


def typed_property(name, expected_type):
    storage_name = '_' + name

    @property
    def prop(self):
        return getattr(self, storage_name)

    @prop.setter
    def prop(self, value):
        if not isinstance(value, expected_type):
            raise TypeError(f"[ {name} ] must be of the {expected_type} type")
        setattr(self, storage_name, value)

    return prop


String = partial(typed_property, expected_type=str)
Int = partial(typed_property, expected_type=int)


class Person:
    name = typed_property('name', str)
    age = typed_property('age', int)
    surname = String('surname')
    count = Int('count')

    def __init__(self, name, age, surname, count):
        self.name = name
        self.age = age
        self.surname = surname
        self.count = count


def main():
    p = Person('Smital', 10, 10, "Desai")
    print(p)


if __name__ == '__main__':
    main()
