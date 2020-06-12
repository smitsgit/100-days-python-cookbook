from inspect import Signature, Parameter


def make_signature(names):
    sig = Signature([Parameter(name, Parameter.POSITIONAL_OR_KEYWORD) for name in names])
    return sig


class Structure:
    __signature__ = make_signature([])

    def __init__(self, *args, **kwargs):
        bound = self.__signature__.bind(*args, **kwargs)
        for name, val in bound.arguments.items():
            setattr(self, name, val)


class Stock(Structure):
    __signature__ = make_signature(['name', 'shares', 'price'])


class Point(Structure):
    __signature__ = make_signature(['x', 'y'])


class Host(Structure):
    __signature__ = make_signature(['address', 'port'])
