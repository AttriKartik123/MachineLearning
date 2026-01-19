class Raman :
    def use(self):
     print("Raman calling...")

class Harleen(Raman) :
     def use(self):
      print("Harleen calling...")

class Karan(Harleen) :
     def use(self):
      print("Karan calling...")

K= Karan()
K.use()  