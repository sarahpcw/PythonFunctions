
from movieFunctionFile import movieFunctions   ### step 1

class movieFunctionFile2 (movieFunctions):    ### step 2

    mynumber = 0
    myname = ""
    def __init__(self, name, number):   
        super().__init__(name, number) ### step 3
        self.mynumber  = number
        
    def calcSquare ( self ):
        m = self.mynumber * self.mynumber 
        print (m)
    
    def printwarning (self ):
        print("Hello", self.myname, "You  can go on HOLIDAY shortly")