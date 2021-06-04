from movieFunctions2 import movieFunctions

class popcorn (movieFunctions):
    tp = 0
    def __init__(self, tp):
        super().__init__(tp)    
        ## super tranfers the value of tp to the input parameter of the __init__ of the parent
        self.tp = tp 
        
    def calcPopcorn( self , a , p , c) :
        popcorn = ( a + p + c ) *  (self.tp * 0.1) 
        return popcorn
        
