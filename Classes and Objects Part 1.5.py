class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight
        # "self" needs to be first argument
        # This is the a constructor
        # Convention is to name the arguments as the attributes we set
    def introduce_self(self): # Need to add "self" inside to
                              #every method you add to a class.
        print("My name is " +self.name) # The self will refer to
                                        # whatever function we are
                                        # running the objet on.
                                        # self leads to object?


r1 = Robot("Tom","red",30) # Create a new objected
r2 = Robot("Jerry","blue",40)


r1.introduce_self() #to run the function in class.
r2.introduce_self()

