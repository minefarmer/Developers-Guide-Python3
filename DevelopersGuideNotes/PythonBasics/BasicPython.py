# Writing Functions   53
# Conditionals: if   72
# Conditionals: else   84
# Conditionals: elif   100
# Conditionals: elif #2   118
# Calculator   137
# 
# 
"""BASIC PYTHON
Variable, is simply a name I use to to allow me to access some value I need to store in memory.
    TYPE CONVERSION
float() used to convert data to the float type.
str() used to convert data to the string type.
int() used to convert data to the integer type.

    SEQUENCES AND COLLECTIONS
list: () a way to create a list of data 
dict: {} to store = key/value pairs

    USER INPUT()
Is a function that prompts the user to input data into my program.
The input from the user is returned from the function and then we can assign it to a variable.

    WRITING FUNCTIONS
        To write my own functions           Example:
1. start with the def keyword           | def print_twice(data_to_print).
2. choose function name                 |    
3. include any arguments I want for     |    print(data_to_print)
   my function to have as var names.    |
4. Use a colon and then indent to start |    print(data_to_print)
    writing the code for my function.

    BOOLEAN EXPRESSIONS
        Definition                              Example:
Evaluates to true or false                  x == 100  # True if x is equal to 100

    CONDITIONAL STATEMENTS: if, else, elif
        Definition if                                 Example:
To create programs with branching logic,        if:<boolean expression>:
conditional statements are necessary
                                                <execute the code here
                                                
        Definition elif                               Example:
                                                else:
                                                <execute the code here
                                                
        Definition else                               Example:
                                                else:
                                                <execute the code here
    
"""


# WRITING fUNCTIONS
# num_1 = input("Please enter a number: ")  # 7
# num_2 = input("Please enter a second number: ")  # 8

# result = int(num_1) + int(num_2)
# print("Your result was: "+ str(result))  # 15


# def add(num1, num2):
#     return int(num1)

# num_1 = input("Please enter a number: ")  # 7
# num_2 = input("Please enter a second number: ")  # 8

# result = int(num_1) + int(num_2)
# print("Your result was: "+ str(result))  # 15



# Conditionals: if
# x = 13
# y = 23

# if x == y:
#     print("This statement should never run")
    
# if y  > x:
#     print("Y is greater than X!")  # Y is greater than X!



# Conditionals: else
# x = 13
# y = 23

# if x ==y:
#     print("This print statement should never run")
# else:
#     print("X is NOT equal to Y!")  # X is NOT equal to Y!

# if y > x:
#     print("Y is greater than X!")  # Y is greater than X!
# else:
#     print("This print statement also, should never run")



# Conditionals: elif
# x = 13
# y = 23

# if x == 1:
#     print("X is equal to 1")
    
# elif x == 2:
#     print("X is equal to 2")
    
# elif x == 3:
#     print("X is equal to 3")
    
# else:
#     print("X is NOT a number from 1-3!")  # X is NOT a number from 1-3!



# Conditionals: elif  # 2
# x = 2
# y = 23

# if x == 1:
#     print("X is equal to 1")
    
# elif x == 2:
#     print("X is equal to 2")  # X is equal to 2
    
# elif x == 3:
#     print("X is equal to 3")
    
# else:
#     print("X is NOT a number from 1-3!")



# Calculator
def add(num1, num2):
    return int(num1) + int(num2)

def subtract(num1, num2):
    return int(num1) - int(num2)

def multiply(num1, num2):
    return int(num1) * int(num2)

def divide(num1, num2):
    return int(num1) / int(num2)

num_1 = input("Please enter a number: ")  

num_2 = input("Please enter a second number: ")

operator = input('select an operation to perform: [add, subtract,multiply, divide]')

if operator == "add":
    result = add(num_1, num_2)
    
elif operator == "subtract":
    result = subtract(num_1, num_2)
    
elif operator == "multiply":
    result = multiply(num_1, num_2)
    
elif operator == "divide":
    result = divide(num_1, num_2)
    
else:
    result = 0
    print("Invalid operator!")

print("Your result was: "+ str(result))