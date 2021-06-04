##### all function definitions
####  step 1 : create a class
####  step 2 : indent all the functions
####  step 3 : use self as the first parameter in every function
####  step 4 : save

class calcs :
    
    def calcArea(self, l, w):
        a = l* w   ## 
        return a   
        ## return value , a value calculated by the function and returned to the function call
    
    def printResults(self, a, cp) :
        print ( 'The area is : ' )
        print (a, "square meters " )
        print ('The price of a carpet of ', a, 'sqm, is' , cp)
        return  ### optional because there is no return value
    
    def calcCarpetPrice (self, area) :
        carpetPrice = area * 10
        return carpetPrice


