

__module_attr = "module1.__attr"


class test1(object):
    __var1 = "test1.__var1"
    nvar1 = "test1.nvar1"

    def test(self):
        self.__var2 = "test1(self).__var2"
        self.__var3__ = "test1(self).__var3__"
        self.nvar2 = "test1(self).nvar2"
        print("test1.__var1:{0}".format(test1.__var1))
        print("test1(self).__var1: {0}".format(self.__var1))
        print("test1(self).__dict__: {0}".format(self.__dict__))


class test2(object):
    def test(self, o):
        o.__var4 = "test2.o.__var4"
        o.__var5__ = "test2.o.__var5__"
        o.nvar3 = "test2.o.nvar3"
        print("test2.o.__dict__:{0}".format(o.__dict__))
