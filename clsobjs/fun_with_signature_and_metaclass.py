from inspect import Signature, Parameter


def make_signature(names):
    sig = Signature([Parameter(name, Parameter.POSITIONAL_OR_KEYWORD) for name in names])
    return sig


class StructMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        clsobj = super().__new__(cls, clsname, bases, clsdict)

        clsobj.__signature__ = make_signature(clsobj._fields)
        return clsobj


class Structure(metaclass=StructMeta):
    _fields = []

    def __init__(self, *args, **kwargs):
        bound = self.__signature__.bind(*args, **kwargs)
        for name, val in bound.arguments.items():
            setattr(self, name, val)


class Stock(Structure):
    _fields = ['name', 'shares', 'price']


class Point(Structure):
    _fields = ['x', 'y']


class Host(Structure):
    _fields = ['address', 'port']
