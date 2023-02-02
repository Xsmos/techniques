class Employee:
    '所有员工的基类'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("total employee {}".format(Employee.empCount))

    def displayEmployee(self):
        print ("Name:", self.name, "; Salary:", self.salary)

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, '销毁')

class Parent:
    parentAttr = 100
    def __init__(self):
        print('调用父类构造函数')

    def parentMethod(self):
        print("调用父类方法")

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print('父类属性：', Parent.parentAttr)

    def myMethod(self):
        print('调用父类myMethod方法')

class Child(Parent):
    def __init__(self):
        print('调用子类构造方法')

    def childMethod(self):
        print('调用子类方法')

    def myMethod(self):
        print("调用子类myMethod方法")

class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector({},{})'.format(self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)

class JustCounter:
    __secretCount = 0
    publicCount = 0

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print('self.__secretCount =', self.__secretCount)

class Runoob:
    __site = 'www.runoob.com'

def test_import_functions(x):
    y = 10*x + 1
    print('function imported well')
    print('result is: ', y)
    print('receive z = ', z)
    return y

def useAnotherFunction(x):
    global z
    z = 'global quantity'
    print('I am using nested function!')
    test_import_functions(x)
    print('ended')
