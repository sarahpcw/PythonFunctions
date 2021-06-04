from cfunction2 import cfunctions2  # from filename import classname
class runClass(cfunctions2):
    
    more = 'yes'
    cq=aq=cq1=aq1=0
    while ( more == 'yes' ):
        coname = input("Please enter your company")
        if coname == 'ABD':
            abc = cfunctions2( coname )
        if coname == 'xyz' :
            xyz = cfunctions2( coname )
        
        
        width   = float ( input ("What is the width?" ) )
        length  = float ( input ("What is the length?") )
        
        if coname == 'ABD':
            area = abc.calcArea (l = length , w = width) # + - * / ()
            price, carpetprice = abc.calcPrice (area)
            print ( "Carpet per sqm %.2f , Please pay %.2f" % ( price , carpetprice) )
            cq = abc.countquotesCustomer()
        
        if coname == 'xyz':
            area = xyz.calcArea (l = length , w = width) # + - * / ()
            price, carpetprice = xyz.calcPrice (area)
            print ( "Carpet per sqm %.2f , Please pay %.2f" % ( price , carpetprice) )
            cq1 = xyz.countquotesCustomer()
        
        
        print ( cq,  cq1 , cfunctions2.count)
        more = input ( 'More quotes? ') 
        
       