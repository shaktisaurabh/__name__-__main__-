import manny1
a=int(input("Enter the number? "))
manny1.square(a)
print(__name__)
print(manny1.__name__)
#as we can see when we import manny1, the entire code of manny1 gets executed before manny2 is executed
#In order to avoid the execution of some un-wanted, private codes of the file that we are importing, we follow
#a different method which has been elaborated in manny3 and manny4 files.
# One thing worth noting is that the value of __name__ variable within the manny1 file is __main__,whereas the
# the value of manny1.__name__ in manny2 file is manny1....__name__ variable stores the name of the module, when a
# file is executed, its name would be __main__ but when it is imported and executed, its name would be different.
# We will exploit this difference to block a part of our code and avoid that part of code from being imported and executed by
# other files in python.We will elaborate this in manny3 and manny4 files.  