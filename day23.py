'''
Multi-Level
-----------
--> This occurs when a class inherit from child class creating a grandparent-->parent-->child
in the structure

class grandparent:
    def show_grandparent(self):
        print("I'm grandparent")

class parent(grandparent):
    def show_parent(self):
        print("I'm parent")

class child(parent):
    def show_child(self):
        print("I'm Child")

obj = child()
obj.show_grandparent()
obj.show_parent()
obj.show_child()

#code2
class chocolates:
    def show_chocolates(self):
        print("I'm Chocolates")
        
class nestle(chocolates):
    def show_nestle(self):
        print("I,m Nestle")

class milkybar(nestle):
    def show_milkybar(self):
        print("I'm Milkybar")

obj = milkybar()
obj.show_chocolates()
obj.show_nestle()
obj.show_milkybar()

Hierarichal
-----------
--> This occurs when multiple child classes inherit from in a single parent class


class parent:
    def parent(self):
        print("I am parent")

class child_1(parent):
    def child1(self):
        print("I am first child")

class child_2(parent):
    def child2(self):
        print("I am second child")

class child_3(child_1,child_2):
    def child(self):
        print("I am the child")

obj = child_3()
obj.parent()
obj.child1()
obj.child2()
obj.child()

Hybrid Inheritance
------------------
--> This is a combination of two or more types of inheritance such as single,multiple,multi-level
or hierarichal

class grandparent:
    def show_grandparent(self):
        print("I'm grandparent")

class parent(grandparent):
    def show_parent(self):
        print("I'm parent")

class child(parent):
    def show_child(self):
        print("I'm Child")


class parent:
    def parent(self):
        print("I am parent")

class child_1(parent):
    def child1(self):
        print("I am first child")

class child_2(parent):
    def child2(self):
        print("I am second child")

class child_3(child_1,child_2,grandparent):
    def child(self):
        print("I am the child")

obj = child_3()
obj.show_grandparent()
obj.parent()
obj.child1()
obj.child2()
obj.child()'''
















    





        
