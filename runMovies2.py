from movieFunctionsExtras import movieFunctionsExtras # from filename import classroom

class runFunctions(movieFunctionsExtras) :  # classname

    adults = c = p = pop = singleticketprice =  0
    weekday = False   # True

    if weekday :
        obj = movieFunctionsExtras(10)
    else: 
        obj = movieFunctionsExtras(20)
    
    #### create the object of child class movieFunctionsExtras
    ## the line above runs the init function
    
    
    movie = obj.findMovieChoice()   # parent
    
    adults , p , c =  obj.askTicketNumbers() # parent # accepts the console input as string 
        
    ticketprice = obj.calcPrice (  adults, c, p)  # child  # call the lambda function
    
    obj.printTickets(movie, adults, c, p, ticketprice)   # parent
 
    pop = obj.calcPopcorn (1.5 , adults, c, p) # child
    print ( "Ticketprice plus popcorn:", (ticketprice + pop))
    
    
    
    
    
    
    
    
    
    
    
    
 



    
#print( movieFunctionsExtras.__doc__)
#print( 'name----', movieFunctionsExtras.__name__)
#print( 'module----\n', movieFunctionsExtras.__module__)
#print( 'bases----\n', movieFunctionsExtras.__bases__)
#print ('dict-----\n')
#for functionname in  movieFunctionsExtras.__dict__: 
#    print ( functionname )
    
  
    
    
    
#
#    obj.p2()
#    obj.p3()
#    
       
        
#    print ( "")
#    obj2 = movieFunctions()
##    adults , p , c =  obj.askTicketNumbers()# accepts the console input as string 
#    if adults == 0 and p == 0:
#        print ( "No children alone allowed")  
#    ticketprice = calcPrice (10, adults, c, p)
#    obj2.printTickets(movie, adults, c, p, ticketprice)
#    pop = obj2.calcPopcorn (1.5 , adults, c, p)
#    print ( "Ticketprice plus popcorn:", (ticketprice + pop))