'''table_num = 8
for j in range(1,11):
    print(f"{table_num} X {j} = {table_num * j}")
#print tables'''

'''String methods :
count(),join(),strip(),replace(),split(),capitalize(),casefold(),
isalnum(),isalpha(),isdigit(),isdecimal(),islower(),isupper()
'''
'''an = "python IS a Programming Language"
count_U = 0
count_L = 0
for ch in an:
    if ch.isupper():
        count_U += 1
    elif ch.islower():
        count_L += 1
print (f" There are total {count_U} cap L ")
print (f" There are total {count_L} small L ")'''

'''an = "python IS a Programming Language"
Cap_L = []
small_L = []
for ch in an:
    if ch.isupper():
        Cap_L.append(ch)
    elif ch.islower():
        small_L.append(ch)
print(f"{Cap_L} contain all Cap L")
print(f"{small_L} contain all small L")'''

'''ICICI_Theekshani_AC_Details = {"Name" : "Theekshani",
                               "ATM PIN" : "0066"}
print ("Welcome to ICICI ATM ")
print ("Pls insert your ATM Card")
ICICI_user_pin = input("Pls enter your 4 digits ATM Pin:")
if len(ICICI_user_pin) == 4:
    if ICICI_user_pin in ICICI_Theekshani_AC_Details['ATM PIN']:
        print("The pin is correct")
    else:
        print("You entered invalid pin")
        
'''

'''per_num = int(input("Enter a number: "))
fact_all = 0
for j in range(1,per_num):
    if per_num % j == 0:
        fact_all += j
if fact_all == per_num:
    print(f"{per_num} is the perfect num")
else:
    print(f"{per_num} is not a perfect num")
#program for perfect number
'''

'''List Methods:

append():-
--------
nums = [8, 10, 29]
nums.append(39)
print(nums)

extend():-
-------
nums = [29, 11]
nums.extend([3, 4, 5])
print(nums)

insert():-
-------
nums = [2, 5, 4]
nums.insert(2, 3)
print(nums)

remove():-
--------
nums = [11, 10, 29, 3]
nums.remove(3)
print(nums)

pop():-
----
nums = [10, 20, 30]
nums.pop(1)
print(nums)

clear():-
-----
nums = [23, 29, 32]
nums.clear()
print(nums)

index():-
-----
nums = [10, 20, 30]
print(nums.index(20))

count():-
-----
nums = [1, 2, 2, 3, 2]
print(nums.count(2))

sort():-
-----
nums = [25563, 716753, 93236, 13512]
nums.sort()
print(nums)

reverse():-
-------
nums = [11, 23, 35]
nums.reverse()
print(nums)

copy():-
-----
nums = [1, 2, 3]
new_list = nums.copy()
print(new_list)'''







