"""EXCEPTIONS
Exceptions are used by python to indicate               Exceptions themselves are just classes, I can
unexpected behavior in my code.                         create my own exceptions by subclassing
                                                        (inheriting from) the build in e\Exception class in python.

Exceptions will halt the execution of my program.


TRY AND EXCEPT
If a piece o code could potentiallyraise an             try:
exception I know about, I can place it in a
try and except block.                                       my_function()

                                                        except:
                                                        
                                                            print("an error occured")


RAISE
The raise keyword will simply raise an exception        raise IndexError
I specify.

I can also create an instance of the exception
to pass the extra information to.

"""
# Exceptions   33
# try and except block   49
# try and except block   67
# raise   82
# 
# 
# 
# 
# myarray = [1,2,3]

# for item in [0,1,2,3,4,5]:
#     print(myarray[item]) # 1
#                         # 2
#                         # 3
#                         # Traceback (most recent call last):
#                         # File "/home/carl/Github/Developers-Guide-Python3/DevelopersGuideNotes/OtherPythonFeatures/exceptions.py", line 16, in <module>
#                         #     print(myarray[item])
#                         # IndexError: list index out of range
                        



# try and except block
# myarray = [1,2,3]

# for item in [0,1,2,3,4,5]:
#     try:
#         print(myarray[item])
#     except:
#         print("The element is not in the list")  # 1
#                                                 # 2
#                                                 # 3
#                                                 # The element is not in the list
#                                                 # The element is not in the list
#                                                 # The element is not in the list
                                                
# print("The program continues to run!")  # The program continues to run!



# try and except block
myarray = {}

for item in [0,1,2,3,4,5]:
    try:
        print(myarray[item])
    except: IndexError
print("The element is not in the list")  # The element is not in the list
                                                
print("The program continues to run!")  # The program continues to run!



# raise
# >> IndexError
# <class 'IndexError'>
# >>> Exception
# <class 'Exception'>
# >>> class MyError(Exception):
# ...     pass
# ... 
# >>> MyError
# <class '__main__.MyError'>
# >>> raise IndexError("The list index is out of range")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: The list index is out of range
# >>> 
