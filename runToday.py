# step 1. import from filename import classname
# step 2. create object
# step3. prefix all function names with the object name
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


from movieFunctionFile2 import movieFunctionFile2

mf = movieFunctionFile2("Peter" , 35 )   
# object  , use the name of the class
# give the name and number values to __init__ of movieFunctionFile2

mf.printmsg()     ## in movieFunctionFile
mf.printgoodbye() ## in movieFunctionFile
mf.calcSub()
mf.calcAdd()
mf.calcMultiply()  ## function call, executes the code in a function
mf.calcDiv()

mf.calcSquare()   ## in movieFunctionFile2

mf.printwarning()  ## in both
## in movieFunctionFile AND in movieFunctionFile2
## executes the printwarning of movieFunctionFile2
## it overrides printwarning in movieFunctionFile












