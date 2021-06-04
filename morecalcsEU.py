from calcs import calcs 

class morecalcsEU (calcs):
    def calcVatEU ( self, cp ) :
        vat = cp * 17 / 100   ## uk
        return vat
        