'''
File handling
-------------
--> File handler is A Object od file to maintain several functions of file
such as creating, reading, writing and update also deleting the file

How to open the file
--------------------
1).open()
---------
--> This open() function takes 2 parameters and in this we have to close the file by calling close() function
after program.
1).file name
2).mode

2).with open()
--------------
Modes ("r","w","a","x","t")
---------------------------
1)"r"-- read --> to read the file you will use this mode and
if the file doesn't exist,it will give the error

any = open("demo.txt","r")
print(any.read())

2)"w"-- write --> To write the text into the file we will use this mode and
it will create the file if it doesn't exist
-->it will over write new text with old text in the file..

3)"a" -- append() --> To add the text into the file this is used and
it will create the file if it doesn't exist

4)"x" -- create --> This is used to create the file, but it is already in the system
it raise an error

To read a file
--------------
1).read()
--> This method can read the entire file chunk by chunk(line by line including spaces).
2).readline()
--> This method can only read one line at a time
3).readlines()
--> This method can read the entire file  and return into list with each line is one index in the list
'''



