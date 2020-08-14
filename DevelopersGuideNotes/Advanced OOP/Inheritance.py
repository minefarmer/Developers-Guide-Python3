"""INHERITANCE
Ineritance is a way for classes to' acquire'                Class Honda(car):
attributes and methods from other classes.
                                                                model = 'Honda Civic'

I cna 'inherit' from anouther class by including            newcar = Car()
it in the parenthesis in your class defination.
                                                            newcar.drive()


OVERRIDING METHODS
If I inherit methods or attributes from a parent            class Car:
class that I want to change in a child class, I
 can override the attribute or method.                          def drive(self)
 
This allows me to change the behavior of a Child                    print("Driving")
class, without making changes to a parent class.
                                                            class HondaCivic(car)
                                                            
                                                                def drive(self):
                                                                    
                                                                    print("Driving my Honda!")


CALLING SUPER()
If I want to preserve the original behavior of an           class Car:
overridden method, I can use super() to get access
to the parent class, and then call it's method.                 def drive(self):

                                                                    super(HondaCivic, self).drive()
                                                                    
                                                                    print("Driving MY Honda")

"""
# 
# 
# 
# 
# 
# 
# 

class Car:
    def __init__(self):
        self.engine = False
        
    def start_engine(self):
        print("Starting Engine")
        self.engine = True
            
    def stop_engine(self):
        print("Stopping engine")
        self.engine = False
        
    def drive(self):
        if self.engine:
            print("Driving the Car!")
        else:
            print("I need to start the engine first!")
            

class HondaCivic(Car):
    model = 'Honda Civic'
    color = 'Blue'
    
    def start_engine(self):
        super().start_engine()
        print("Honda! Start Engine")
        self.engine = True
    