'''MODULES
            my_program.py                   My python program may consist of multipule files.
            /            \                    I may want to organize my code into what's known as a module
           /              \
        functions.py    classes.py


THE IMPORT KEYWORD
The import keyword, brings a module into my             import math
current python program or interpreter sesion,
and alows me to access that module's functions          print(math.pi)  # 3.141592653589793
and attributes.
                                                        from math import pi
A module is just a python file(.py extension)
                                                        print(pi)
I can use the from keyword to import something
specific from a module,


'''
# 
# 
# 
# 
# 
# Importing modules
# import math
# print(math.pi)  # 3.141592653589793

# print(math.factorial(4))  # 24

# from math import pi
# print(pi)  # 3.141592653589793

from math import factorial, pi
print(pi)  # 3.141592653589793
factorial(3)
print(factorial(3))  # 6
