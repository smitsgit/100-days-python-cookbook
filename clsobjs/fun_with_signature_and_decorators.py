from inspect import Signature, Parameter


def make_signature(names):
    sig = Signature([Parameter(name, Parameter.POSITIONAL_OR_KEYWORD) for name in names])
    return sig


def add_signature(*names):
    def decorator(cls):
        cls.__signature__ = make_signature(names)
        return cls

    return decorator


class Structure:
    __signature__ = make_signature([])

    def __init__(self, *args, **kwargs):
        bound = self.__signature__.bind(*args, **kwargs)
        for name, val in bound.arguments.items():
            setattr(self, name, val)


@add_signature('name', 'shares', 'price')
class Stock(Structure):
    pass


@add_signature('x', 'y')
class Point(Structure):
    pass


@add_signature('address', 'port')
class Host(Structure):
    pass
