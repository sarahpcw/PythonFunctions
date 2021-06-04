# initialise a value that is used throughout a class (class variable)
# __init__ runs when I make an object
# it does not run again
# I cannot call the __init__ function again
# initialise class variables , as a parameter of the object

# class variable : self.variablename

# inheritance
# parent/child structure
# create object of the child which imports everything from the parent

# override: 2 functions with the same and input parameters
# the version of the function found in the child class will be executed

from movieFunctions import movieFunctions
 
class moviePopcorn(movieFunctions): 
    spopprice = 0
    def __init__(self, stp, p):
        super().__init__(stp)
        self.spopprice = p
    
    def addPopcorn ( self ,  nr ):
        popcornPrice = nr * self.spopprice
        return popcornPrice
    
    def p2 (self ):
        print ( 'Welcome to the movies in London' )
        print ( 'We welcome you back after lockdown' )
        print ( 'Please wear a face mask and stand 2 meter apart' )
        