## function, paremeter, return value
# class
# object
# objectname
# inheritance
# override
#  constructor __init__
#  parametised constructor
#  super().init(self, variable) # sends a value to the parameter of the init frunction of parent

from calcs import calcs 

class morecalcsUK (calcs) : 
    sname = ''
    def __init__( self, shopname ):
        self.sname = shopname
        print('Welcome to ', self.sname )
        
        
    def calcVat ( self,cp ) :
        print( self.sname )
        vat = cp * 20 / 100   ## uk
        return vat
    
    # override : overrides calcCarpetPrice in the parent class
    def calcCarpetPrice ( self, area ) :  # sigature line of the function
        print( self.sname )
        carpetPrice = area * 10 * 1.1 
        return carpetPrice    