from movieFunctions import movieFunctions # from filename import classroom

class runFunctions(movieFunctions) :  # classname
    
    calcPrice = lambda pr, a, c, p: (a*pr) + (c*pr/2) + (pr*p*0.3)
   
    obj = movieFunctions()
    
    adults = c = p = pop = 0
    
    print ( "Bambi, Rambo , SChrek " )   # this is a comment, ignored by the computer
    movie = input ("Which movie? ")       #  String or text or character  ""  ''
    print(movie)
    
    adults , p , c =  obj.askTicketNumbers()# accepts the console input as string
    
    if adults == 0 and p == 0:
        print ( "No children alone allowed")
    
    ticketprice = calcPrice (10, adults, c, p)
    
    obj.printTickets(movie, adults, c, p, ticketprice)
#    pop = obj.calcPopcorn (1.5 , adults, c, p)
#    print ( "Ticketprice plus popcorn:", (ticketprice + pop))