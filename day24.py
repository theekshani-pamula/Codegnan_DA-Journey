'''
Polymorphism
------------
--> This allows a object of different classes to be treated as instance as the same base class ,
with methods behaving differently based on the actual object type.
print(len("python"))
print(len([1,2,3])

method overloading
------------------
--> This defines multiple methods with same name but different parameters such as numbers,type,or order)
(using extra calling function is called as method overloading)


class calculator:
    def add(self, a, b=0, c=0):
        return a+b+c
cal = calculator()
print(cal.add(2))
print(cal.add(3,4))
print(cal.add(5,7,8))

class calculator:
    def add(self, a, b=0, c=0):
        return a-b-c
cal = calculator()
print(cal.add(2))
print(cal.add(3,4))
print(cal.add(5,7,8))

method overriding
-----------------
--> This occurs in the child class, redefining a parent class method with the same signature for runtime

class animal:
    def speak(self):
        return "sound"

class dog(animal):
    def speak(self):
        return "bow bow"

Dog = dog()
print(Dog.speak())

operator overloading
--------------------
--> This customizes operators like +,- for user defined classes by implementing special methods....
eg... __add__,__sub__ 

class someone:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return someone(self.a + other.a, self.b + other.b)
    def __str__(self):
        return f"({self.a}, {self.b})"
obj = someone(2,3)
so = someone(5,9)
print(obj + so)


data abstraction
----------------
--> This hides complex implementation details, exposing only essential features via abstract class or interface.
'''

from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
class circle(shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius **2
Circle = circle(7)
print(Circle.area())
    
      










