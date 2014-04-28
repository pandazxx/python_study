__author__ = 'pandazxx'

from utilities import trace


class DummyObject(object):
    @trace
    def __init__(self, *args, **kwargs):
        self.__args = args
        self.__kwargs = kwargs

class DecoratorExample(object):
    @trace
    def __init__(self, name, defval):
        self.__name = name
        self.__val = defval

    @trace
    def __get__(self, instance, owner):
        return self.__val

    @trace
    def __set__(self, instance, value):
        self.__val = value


class AttrRefBase(object):
    class_attr1 = "class_attr1"
    class_attr2 = DummyObject('1', '2', first='first', second='second')
    decorator_attr1 = DecoratorExample(name='decorator_attr1', defval=10)

    @trace
    def __new__(cls, *args, **kwargs):
        return super(AttrRefBase, cls).__new__(cls, *args, **kwargs)

    @trace
    def __init__(self):
        pass


def main():
    print('AttrRefBase.class_attr2: {0}'.format(str(AttrRefBase.class_attr2)))
    print('AttrRefBase.__dict__: {0}'.format(str(AttrRefBase.__dict__)))
    print('dir(AttrRefBase): {dir}'.format(dir=dir(AttrRefBase)))
    print('isinstance(AttrRefBase, type): {0}'.format(isinstance(AttrRefBase, type)))
    arb = AttrRefBase()
    arb.class_attr1
    arb.decorator_attr1
    arb.decorator_attr1 = 20
    print('arb.class_attr2: {0}'.format(str(arb.class_attr2)))
    print('arb.__dict__: {0}'.format(str(arb.__dict__)))
    print('dir(arb): {dir}'.format(dir=dir(arb)))
    arb.class_attr2 = DummyObject()
    print('arb.__dict__: {0}'.format(str(arb.__dict__)))



if __name__ == '__main__':
    main()