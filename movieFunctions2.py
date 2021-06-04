#1. Create a class
#2. indent everything in the class
#3. use the keyword self , must be the first parameter in all the functions

class movieFunctions:
    tp = 0
    def __init__(self, price):
        self.tp = price
    
    def askTicketNumbers (  self ):
        a = int ( input ( "How many adults want to buy a movie ticket? "))
        p = int ( input ( "How many pensioners want to buy a movie ticket? "))
        c = int ( input ( "How many Children want to buy a movie ticket? "))
        return a,p,c
    
    def calcTp ( self, a,p,c ):
        return a * self.tp + (p* self.tp/3) + (c * self.tp / 2)

    def printTickets( self , movie, adults, c, p,  ticketprice):
        print ( "Your movie choice:", movie, 'and the single ticket price is' , self.tp )
        
        print ( "Ticket ordered: ")
        
        if adults > 0 : 
            print ( "Adults:", adults)
        if c > 0:
            print ( "Children:",c)
        if p > 0:
            print ( "Pensioners:",p) 
        
        print ( "Total Price:", ticketprice)

