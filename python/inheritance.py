class ParentClass:

    def method1(self):
        print('this is method 1 from parent')

    def method2(self):
        print('this is method 2 from parent')


class ChildClass(ParentClass):  # Inherited Parent class

    def method3(self):
        print('this is method 3 from child')

    def method4(self):
        print('this is method 4 from child')


obj_parent = ParentClass()

obj_child = ChildClass()
obj_child.method1()
obj_child.method2()
obj_child.method3()
obj_child.method4()


