def calcs ( x):
    return x * 2

x = calcs (2)
print ( 'print return value ', x)

calc_times2 = lambda x : x * 2 
print ( ' input is 2' , calc_times2 ( 2 ) )
print ( ' input is 33' , calc_times2 ( 33 ) )
print ( ' input is 51' , calc_times2 ( 51 ) )
print ( ' input is 10' , calc_times2 ( 10 ) )

calc_Addition = lambda x,y : x + y 
print ( ' 2 plus 3 :' , calc_Addition( 2,3 ))
print ( ' 3 plus 3 :' , calc_Addition( 3,3 ))
print ( ' 5 plus 1 :' , calc_Addition( 5,1 ))
print ( ' 1 plus 0 :' , calc_Addition( 1,0 ))


calcMovieTicket = lambda pr, a, c, p : pr*a +(pr*c/2) + (pr*p*0.3)

adults = 1
children = 1  # children pay half
pensioners = 1 # pay 30%
ticket = 10
print ( "TotalPrice" , calcMovieTicket(ticket,adults,children,pensioners))


# runs the function for each value in the list, returning a map object
values = [2,33,51,10]
outvalues = map ( lambda x : x * 2 , values)
print (outvalues)
for val in outvalues :
    print ('output values x * 2 ',val)

Celcius = [27.2 , 26.7 ,24.2 ,38.5]
Fahrenheit = map ( lambda x : (x  *  9/5 ) + 32   , Celcius ) 
print ( type ( Fahrenheit ) )   # Fahrenheit is not a list , it is a map
print ( Fahrenheit)
for each in Fahrenheit: 
    print (each)
    
# if I want to also access Celcius using corresponding indexes
# convert Fahrenheit to a list
Celcius = [27.2 , 26.7 ,24.2 ,38.5]
Fahrenheit =    list ( map  ( lambda x : (x  *  9/5 ) + 32   ,  Celcius ) )
print ( type ( Fahrenheit ) , Fahrenheit)

for i  in range (len(Fahrenheit))  :
    print ('Fahrenheit vs Celcius ' , Fahrenheit[i], ' ' , Celcius[i]  ) 
  

    





