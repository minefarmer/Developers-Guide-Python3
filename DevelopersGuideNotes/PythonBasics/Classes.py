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
        
    def start_engine(self):
        if self.engine == 'off':
            print("Starting Engine")
            self.engine = 'on'
        else:
            print("The engine is already running!")
            
    def stop_engine(self):
        if self.engine == 'on':
            print("Stopping engine")
            self.engine = 'off'
        else:
            print("The engine is already off")
    
    def drive(self):
        if self.engine == 'on':
            print("Driving the car!")
        else:
            print("The engine needs to be started first")
    
    def display_car(self):
        print(self.color)
        print(self.model)
        print("the engine is " + self.engine)
        
    
        
class Car:
    color = 'blue'
    def drive(self):
        print("Driving the car!")
    def paint_car(self, color):
        self.car_color = color

mycar = Car()

    
