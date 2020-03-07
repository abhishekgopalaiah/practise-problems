class GrandParentClass:

    def method1(self):
        print('this is method 1 from GrandParent')

    def method2(self):
        print('this is method 2 from GrandParent')


class ParentClass(GrandParentClass):

    def method3(self):
        print('this is method 3 from parent')

    def method4(self):
        print('this is method 4 from parent')


class ChildClass(ParentClass):

    def method5(self):
        print('this is method 5 from child')

    def method6(self):
        print('this is method 6 from child')


obj_grand_parent = GrandParentClass()
obj_parent = ParentClass()
obj_child = ChildClass()

obj_child.method1()
obj_child.method2()
obj_child.method3()
obj_child.method4()
obj_child.method5()
obj_child.method6()
