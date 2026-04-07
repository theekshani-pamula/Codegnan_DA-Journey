'''
Required arguments
------------------
--> It should match same number variables in calling with def'''

'''num_1 = 9
num_2 = 10
def add(num_1,num_2):
    print(num_1 + num_2)
add(num_1, num_2)'''

'''
Default Arguments
-----------------
--> it will take the default values from the arguments

My_name = "Honey"
def add(My_name):
    print(My_name)
add(My_name = "Pamula")


def prime_no(num,count):
    for j in range(1,num+1):
        if num % j == 0:
            count += 1
    if count == 2:
        print(f"{num} is a prime")
    else:
        print(f"{num} is not prime")
prime_no(num = 7,count = 0)
prime_no(num = 47,count = 0)
prime_no(num = 6, count = 0)'''

'''
keyword Arguments
-----------------
-->


def any(num, num_3, num_2):
    print(f"num = {num}, num_2 = {num_2},num_3 = {num_3}")
any(num_2 = 29,num = 11,num_3 = 20)

def birds(b_2 ,b_1,b_3):
    print(f" b_1 = {b_1},b_2 = {b_2},b_3 = {b_3}")
birds(b_2 = "Eagle" , b_1 = "Kingfisher" , b_3 = "parrot")'''



'''
Variable length Arguments
-------------------------

--> Adding a star(*) before the parameter name in the function, receive a tuple of arguments and can access indexes

def name(*student):
    print(student[2])
name("Theeku" , "Honey" ,"chutki")

'''

'''
#count number of words in a sentence
sentence = "My name is Theekshani , I am from Vizag"
words = sentence.split()
count = len(words)
print("Number of words:", count)

num = [1,2,29]
num_2 = num.append(11)
print(num)'''

'''
#compound interest program
principle = 2000
rate = 6
time = 2
CI = principle * (1 + rate/100)** time - principle
print("compound Interest =" , CI)'''

'''














































