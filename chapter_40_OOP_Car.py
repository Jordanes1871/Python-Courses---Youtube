class Car:


    #class variable is defined inside a class but outside the constructor 
    wheels = 4 #class variable by default all cars will have 4 wheels i.e. like a default values for each obj you create within class
    
    

    # init method = constructor 
    def __init__(self, make, model, year, color): # where we pass in different objects, make, model etc
        self.make = make            #instance variables
        self.model = model          #instance variables
        self.year = year            #instance variables
        self.color = color          #instance variables
    
    def drive(self):
        print("This " + self.make +" " + self.model + " is driving")
        
    def stop(self):
        print("This "+ self.make +" " + self.model + " has stopped")