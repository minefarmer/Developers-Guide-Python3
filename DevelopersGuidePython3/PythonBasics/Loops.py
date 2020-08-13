"""LOOPING
    While loop
        Description                                 Example
Loops until the loops conditions are met        while(<boolean expression>)
                                                    <execute the code here until the condition is false.

    For loop
            Description                                 Example
the for loop will execute all of the code within
the body of the loop, once for each element of      for <variable name> in <sequence_name>:
the sequence that's passed.                         
                                                    <execute the code here until we've exhasted the sequence>    


    Advanced looping: break, continue
If I need to change the flow of code execution in my loop for any reason, I can use break and continue statements.
Break will break out of the loop.
continue will restart the loop without execution the code after the continue statement.


"""
# While Loop   22
# For Loop   32
# For Loop   57
# 
#
# 
# 
# While Loop
# print_number = 3
# while print_number != 0:
#     print("Hello World!")  # Hello World!
#                             # Hello World!
#                             # Hello World!
#     print_number = print_number-1
    
    

#  For Loop
# nums = [2,4,6,8]
# for value in nums:  # 2
#                     # 4
#                     # 6
#                     # 8
#     print(value)
    

# mystring = "Hello World"
# for character in mystring:
#     print(character)  # H
#                     # e
#                     # l
#                     # l
#                     # o
                    
#                     # W
#                     # o
#                     # r
#                     # l
#                     # d



# # For Loop # 2
# def sum_list(mylist):
#     list_sum = 0
#     for number in mylist:
#         list_sum = list_sum + number
#     return list_sum

# def list_contains(mylist, element):
#     for el in mylist:
#         if el == element:  # 3 
#             print("Yes")  # Yes

# print(sum_list((5,6,7,8)))  # 26

# list_contains([2,4,6,8], 10)

# list_contains([2,4,6,8], 2)




# # Break  1
# def sum_list(mylist):
#     list_sum = 0
#     for number in mylist:
#         list_sum = list_sum + number
#     return list_sum

# def list_contains(mylist, element):
#     for el in mylist:
#         if el == element:  # 3 
#             print("Yes")  # Yes
#             break

# print(sum_list((5,6,7,8)))  # 26

# list_contains([2,4,6,8,2], 2) 



# Break  1
def sum_list(mylist):
    list_sum = 0
    for number in mylist:
        list_sum = list_sum + number
    return list_sum

def list_contains(mylist, element):
    for el in mylist:
        if el == element:  # 3 
            print("Yes")  # Yes
            break

print(sum_list((5,6,7,8)))  # 26

list_contains([2,4,6,8,2], 2) 