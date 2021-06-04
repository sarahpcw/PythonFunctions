adults = c = p = 0

print ( "Bambi, Rambo , SChrek " )   # this is a comment, ignored by the computer
movie = input ("Which movie? ")       #  String or text or character  ""  ''
print(movie)

adults = input( "How many adults want to buy a movie ticket? ") # accepts the console input as string
adults = int(adults)
 
p = input( "How many pensioners want to buy a movie ticket? ") # accepts the console input as string
p = int(p)

if adults > 0 or p > 0:
    c = input( "How many children want to buy a movie ticket? ") # accepts the console input as string
    c = int(c)

price = 10.0
ticketprice = ( adults * price) + ( c * price / 2  ) +  (  p * 0.3  ) 

print ( "Your movie choice:".ljust(20), movie)
print ( "Ticket ordered: ")
if adults > 0 : 
    print ( "Adults:".ljust(20), adults)
if c > 0:
    print ( "Children:".ljust(20),c)
if p > 0:
    print ( "Pensioners:".ljust(20),p)

print ( "Total Price:".ljust(20), ticketprice)

