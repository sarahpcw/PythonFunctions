#1. Create a class
#2. indent everything in the class
#3. use the keyword self , must be the first parameter in all the functions

class movieFunctions:
    myname = ""
    mynumber = 0
    def __init__ (self , name, number):  
        self.myname = name
        self.mynumber = number
#        skdfjls
 
    def printmsg ( self  ):  # signature line
        print ( "hello" , self.myname)
        
    def printgoodbye (self):
        print ("good bye" , self.myname)
    
    def printwarning (self ):
        print("Hello", self.myname, "you will be arrested shortly")
        
    def calcMultiply (self ):
        m = self.mynumber * 2
        print("multiply by 2", self.mynumber, m)
    
    def calcDiv (self ):
        m = self.mynumber / 4.3
        print("divide by 4.3", self.mynumber, m)
    
    def calcSub (self ):
        m = self.mynumber - 9
        print("subtract 9", self.mynumber, m)
    
    def calcAdd (self ):
        m = self.mynumber + 11
        print("add 112", self.mynumber, m)
    
        """
number = 35
create a function in the function library
-  that wil use this number and multiply it by 2
-  print the result

create a function in the function library
-  that wil use this number and divide it by 4.3
-  print the result

create a function in the function library
-  that wil use this number and subtract 9 from it 
-  print the result

create a function in the function library
-  that wil use this number and add 11 to it
-  print the result
"""
        
  
