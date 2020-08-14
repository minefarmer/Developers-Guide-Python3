"""CLASSES
Objects are a way to describe related sets              Class car(object):
of information.                                             def drive(self):
                                                                print("Drive!")


Classes are ways to describe objects                    newcar = Car()

                                                        newcar.drive
                                                        
                                                        

Special methods:__init__
If I want to assign some instance variables             Class BankAccount:
or add parameters to my constructor, I can
define a special function called __init__that               def __init__(self. money)
will be my class constructor.
                                                                self.balance = money
"""
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
class Car:
    def __init__(self, color, model):
        self.color = color
        self.model = model
        self.engine = 'off'
        
    
        
mycar - Car('red')
