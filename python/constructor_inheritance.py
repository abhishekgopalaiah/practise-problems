# class ClassA:
#
#     def __init__(self):
#         print("constructor in ClassA")
#
#
# obj_a = ClassA()
#
# Output:
# constructor in ClassA


# class ParentClass:
#
#     def __init__(self):
#         print("constructor in Parent class")
#
#
# class ChildClass(ParentClass):  # Inherited Parent class
#
#     def __init__(self):  # constructor
#         print("constructor in Child class")
#
#
# obj_child = ChildClass()
#
# Output:
# constructor in Child class

# class ParentClass:
#
#     def __init__(self):
#         print("constructor in Parent class")
#
#
# class ChildClass(ParentClass):  # Inherited Parent class
#
#     def __init__(self): # ChildClass constructor
#         super().__init__()  # calls ParentClass constructor
#         print("constructor in Child class")
#
#
# obj_child = ChildClass()
#
# Output:
# constructor in Parent class
# constructor in Child class


# Method Resolution Order
class BaseClassA:

    def __init__(self):
        print('constructor in BaseClassA')


class BaseClassB:

    def __init__(self):
        print('constructor in BaseClassB')


class DerivedClassC(BaseClassA, BaseClassB):  # Multiple Inheritance

    def __init__(self):
        super().__init__()
        print('constructor in DerivedClassC')


if __name__ == "__main__":
    obj_c = DerivedClassC()  # instance of DerivedClassC has features of other 2 base class

# Output:
# constructor in BaseClassA
# constructor in DerivedClassC