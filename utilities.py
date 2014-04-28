__author__ = 'pandazxx'


def trace(obj):
    if callable(obj):
        def __decorator(*args, **kwargs):
            print("Invoking function: {0}".format(obj.__name__))
            print('With args: {0}'.format(str(args)))
            print('   kwargs: {0}'.format(str(kwargs)))
            ret = obj(*args, **kwargs)
            print('End invoking function {0}, with returning value: {1}'.format(obj.__name__, str(ret)))
            return ret

        return __decorator

def main():
    @trace
    def test_func(*args, **kwargs):
        print("In test func")
        print("args: {0}".format(str(args)))
        print('kwargs: {0}'.format(str(kwargs)))

    test_func('1', '2', '3', first='first', second='second')

if __name__ == '__main__':
    main()

