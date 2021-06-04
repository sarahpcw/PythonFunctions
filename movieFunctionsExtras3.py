from  movieFunctions import  movieFunctions
class movieFunctionsExtras(movieFunctions):
    
        def __init__(self, pr):
            # cannot be called 
            # runs when I create the object 
            self.pr = pr
            print ( "Welcome to the movies" )
            super().__init__(pr)
            
        calcPrice = lambda  self, a, c, p: (a*self.pr) + (c*self.pr/2) + (self.pr*p*0.3)
    
        def calcPopcorn ( self , popprice , a,c,p ):
            return popprice * ( a + c + p)
        
        def printTickets( self , movie, adults, c, p, ticketprice):
            print ( "Your movie choice:".ljust(20), movie)
            print ( "Ticket ordered: ")
            print ( "Adults:".ljust(20), adults)
            print ( "Children:".ljust(20),c)
            print ( "Pensioners:".ljust(20),p) 
            print ( "Total Price:".ljust(20), ticketprice)