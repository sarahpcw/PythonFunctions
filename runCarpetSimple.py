from carpetFunctionDefinitionsUK import carpetFunctionDefinitionsUK   # from filename import classname , specifies where code is to be found

obj = carpetFunctionDefinitionsUK( 10 , "London")        # create a memory resident copy of the class and all its functions
                    # create an object of class cf
                    # create an instance of class cf
                    # instantiate class cf
########## main flow of the program, here I call or execute the functions
# prefix all function names with the object name
w,l =  obj.carpetlengthWidth()
#
area = w * l       # + - * / () 
print ( "Area", area )
#
if area > 1000 :
    print ( "Too big for us, sorry!")
elif area < 5:
    print ( "Too small for us, sorry!")
else:
    cp = obj.calcprice(area)  ## which version of calcprice is used : the one in the child (override)
    print ( "Carpet price ", "$%.2f" % cp)
    d = obj.calcdiscount(area)
    print ( 'Discount     ' , d )
    finalprice = cp - ( cp * d )
    print ( 'Final price before Vat  ' , "$%.2f" % finalprice)
    obj.calcVat(finalprice)
    
    
print ("The end")

