class Raman :
    pen= 'parker'

class Harleen(Raman) :
    pencil= 'Nataraj'

class Karan(Harleen) :
    eraser = 'Doms'

    def use(self):
        print(self.pen) 
        print(self.pencil)    
        print(self.eraser)

K= Karan()
K.use()  