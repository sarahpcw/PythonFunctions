from functionschild import functionschild   # from filename import classname

movies = [['rocky','schrek','big','bambi','scarface','starwars','rambo'] ,
        ['mon','tue','wed','thu','fri','sat','sun'],
        ['10','12','13','14','15','15','17'],
        ['drama','family','comedy','family','crime','fantsy','action']]

mf = functionschild(1.2)  # object of a class or an instance of a class

mf.print_this(movies)

movie=input("Which movie? ")
price = mf.calprice (movie)
print (price)


mf.printvat()

#Create a function that will Print the movie program
#Input Parament: the movies list
#
#rockY, mon,  10 , drama
#shrek.....