'''
Functions():- This is a block of code which is resusble.
-->there are two types 1.built-in or In-build and 2.user-define functions
1.built-in or In-build
----------------------
--> it comes with program which are already defined....
eg: print(),sum(),map().....

2.user-define functions
-----------------------
--> this is created by person who is developing or using for development

note:-
--> it starts with the def keyword followed by the function name
--> and it has calling function...

func syntax:
def func_name(a,b):
    ----------
    ----------
    ----------
func_name()'''

'''a = 10
def func_name(a):#definition function
    if a%2 == 0:
        print(f" {a} is even")
    else :
        print(f" {a} is odd")
func_name(a=2)#calling function'''

'''prime_num = 7
count = 0
def prime_check(Num,k):
    for j in range(1,Num+1):
        if Num % j == 0:
            k += 1
        if k == 2:
            print("prime")
        else:
            print("Not")
prime_check(prime_num,count)'''

'''a = [5,6]
b = [5,6]
print(a == b)# == is making equal directly'''

'''a = [5,6]
b = [5,6]
c = b
print(id(a), id(b))
print(c is b)# is used to look for object'''



















