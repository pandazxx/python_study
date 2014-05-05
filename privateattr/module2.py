

def test3(o):
    o.__var6 = "test3.o.__var6"
    o.__var7__ = "test3.o.__var7__"
    print("test3.o.__dict__:{0}".format(o.__dict__))


if __name__ == "__main__":
    import module1
    t1 = module1.test1()
    t1.test()
    t2 = module1.test2()
    t2.test(t1)
    test3(t1)
    module1.__module_attr2 = "module1.__module_attr2"
    print("module1.__dict__[__module_attr]:{0}".format(module1.__dict__.get('__module_attr', None)))
    print("module1.__dict__[__module_attr2]:{0}".format(module1.__dict__.get('__module_attr2', None)))
