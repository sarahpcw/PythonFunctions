#1. Create a class
#2. indent everything in the class
#3. use the keyword self , must be the first parameter in all the functions

#### Parent
class movieFunctions:
    singleTicketPrice = 0
    def __init__(self , stp):
        print ( "Welcome to the movies (init) " )
        self.singleTicketPrice = stp
    
    def findMovieChoice( self ):
            print ( "Bambi, Rambo , SChrek " )   # this is a comment, ignored by the computer
            movie = input ("Which movie? ")       #  String or text or character  ""  ''
            print(" Your movie choice", movie)
            return ( movie )
            
    def askTicketNumbers (  self ): 
        a = int( input ( "How many adults want to buy a movie ticket? "))
        p = int( input ( "How many pensioners want to buy a movie ticket? "))
        c = int( input ( "How many Children want to buy a movie ticket? "))
        return a,p,c

    def printTickets( self , movie, adults, c, p, totalTicketPrice):
        
        print ( "Your movie choice:".ljust(20), movie)
        print ( "the single ticket price" , self.singleTicketPrice)
        print ( "Ticket ordered: ")
        if adults > 0 : 
            print ( "Adults:".ljust(20), adults)
        if c > 0:
            print ( "Children:".ljust(20),c)
        if p > 0:
            print ( "Pensioners:".ljust(20),p) 
            
        print ( "Total Price:".ljust(20), totalTicketPrice)
        
        
    def p2 (self  ):
        print ( 'Welcome to the movies' )
