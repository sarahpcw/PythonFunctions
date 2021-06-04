from  movieFunctions import  movieFunctions
class movieFunctionsExtras(movieFunctions):
    
        def __init__(self, pr):   # this parameter pr recives value from where the object is created
            # cannot be called 
            # runs when I create the object 
            super().__init__(pr)    # init of child communicates with init of parent
            print ( "Welcome to the movies" )
            self.price = pr
            
        calcPrice = lambda self,   a, c, p: (a*self.price) + (c*self.price/2) + (self.price*p*0.3)
    
        def calcPopcorn ( self , popprice , a,c,p ):
            return popprice * ( a + c + p)
        
        def printTickets( self , movie, adults, c, p, ticketprice):
            print ( "Your movie choice:".ljust(20), movie)
            print ( " the single ticket price for adults is ", self.pr)   # this line is new, single ticket price
            print ( "Ticket ordered: ")
            print ( "Adults:".ljust(20), adults)
            print ( "Children:".ljust(20),c)
            print ( "Pensioners:".ljust(20),p) 
            print ( "Total Price:".ljust(20), ticketprice)