class BaseClassA:

    def method1(self):
        print('this is method 1 from BaseClassA')

    def method2(self):
        print('this is method 2 from BaseClassA')


class BaseClassB:

    def method3(self):
        print('this is method 3 from BaseClassB')

    def method4(self):
        print('this is method 4 from BaseClassB')


class DerivedClassC(BaseClassA, BaseClassB):  # Multiple Inheritance

    def method5(self):
        print('this is method 5 from DerivedClassC')


if __name__ == "__main__":
    obj_c = DerivedClassC()  # instance of DerivedClassC has features of other 2 base class
    obj_c.method1()
    obj_c.method2()
    obj_c.method3()
    obj_c.method4()
    obj_c.method5()