#### Class ####

# Classes are blueprints where you can make objects
# Objects contain different variables and methods (function)

# Differences between a class and an object is that the values that belong
# to the variables are not defined. It will not refer to a specific object.

# class Robot:
#   def introduce_self(self):
#       print("My name is "+self.name) #self is like "this" in Java
#
# r1 = Robot() #Python constructor(?)
# r1.name = "Tom"
# r1.color = "red"
# r1.weight = 30
# Here a new object has been created and been assigned to r1
# and the attributes have been set.
#
# r1.introdue_self()
#
# r2.Robot()
# r2.name = 'Jerry'
# r2.color = 'blue'
# r2.weight = 40

# r1.introduce_self()

#### Another way to do it with constructors ####
# class Robot:
#   def __init__(self,Name,Color,Weight): # this is a constructor #need self
#       self.name = givenName
#       self.color = givenColor
#       self.weight = givenWeight
#
#   def introduce_self(self):
#       print("My name is "+self.name) #self is like "this" in Java
#
#
# r1 = Robot("tom","red",30)
# r2 = Robot("Jerry","blue",40)
#
# r1.introduce_self()
# r2.introduce_self()
#
#
#
# class Person:
#   def __init__(self,n,p,):
#   self.name = n
#   self.personality = p
#   self.is_sitting = i
#
#   def sit_down(self):
#       self.is+sitting = True
#   def stand_up(self):
#       sef.is_sitting= False
